from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DetailView, ListView

from .forms import BlogSearchForm, CommentForm
from .models import Category, Post


class BlogListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    paginate_by = 6

    def get_queryset(self):
        queryset = Post.objects.published()
        self.search_form = BlogSearchForm(self.request.GET)
        if self.search_form.is_valid():
            query = self.search_form.cleaned_data.get("q")
            if query:
                queryset = queryset.filter(
                    Q(title__icontains=query)
                    | Q(summary__icontains=query)
                    | Q(content__icontains=query)
                    | Q(tags__name__icontains=query)
                    | Q(category__name__icontains=query)
                ).distinct()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = self.search_form
        context["categories"] = Category.objects.all()
        context["featured_posts"] = Post.objects.published()[:3]
        return context


class CategoryPostListView(BlogListView):
    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs["slug"])
        return super().get_queryset().filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = self.category
        return context


class BlogDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_queryset(self):
        return Post.objects.published().prefetch_related("tags", "comments")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comment_form"] = CommentForm()
        context["approved_comments"] = self.object.comments.filter(approved=True)
        context["related_posts"] = (
            Post.objects.published()
            .filter(category=self.object.category)
            .exclude(pk=self.object.pk)[:3]
        )
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.save()
            messages.success(request, "Thanks. Your comment is awaiting approval.")
        else:
            messages.error(request, "Please check the comment form.")
        return redirect(self.object.get_absolute_url())
