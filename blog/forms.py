from django import forms

from .models import Comment


class BlogSearchForm(forms.Form):
    q = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={"placeholder": "Search articles"}))


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["name", "email", "body"]
        widgets = {
            "body": forms.Textarea(attrs={"rows": 4}),
        }
