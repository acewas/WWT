from django.db import models
from django.urls import reverse


class Service(models.Model):
    SERVICE_AREAS = [
        ("technology", "Technology"),
        ("energy", "Sustainable Energy"),
        ("design", "Strategic Design"),
        ("advocacy", "Advocacy"),
    ]

    title = models.CharField(max_length=140)
    slug = models.SlugField(unique=True, null=True, blank=True)
    area = models.CharField(max_length=40, choices=SERVICE_AREAS, default="technology")
    summary = models.TextField()
    description = models.TextField(blank=True)
    technologies = models.TextField(blank=True, help_text="One technology per line")
    industries = models.TextField(blank=True, help_text="One industry per line")
    benefits = models.TextField(blank=True, help_text="One benefit per line")
    icon = models.CharField(max_length=60, blank=True, help_text="Bootstrap icon class or short label")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "title"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("service_detail", kwargs={"slug": self.slug})

    def technology_list(self):
        return _lines(self.technologies)

    def industry_list(self):
        return _lines(self.industries)

    def benefit_list(self):
        return _lines(self.benefits)


class Product(models.Model):
    name = models.CharField(max_length=140)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to="products/", blank=True)
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class TeamMember(models.Model):
    name = models.CharField(max_length=120)
    role = models.CharField(max_length=140)
    bio = models.TextField()
    photo = models.ImageField(upload_to="team/", blank=True)
    linkedin = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "name"]

    def __str__(self):
        return self.name


class Partner(models.Model):
    name = models.CharField(max_length=140)
    description = models.TextField(blank=True)
    logo = models.ImageField(upload_to="partners/", blank=True)
    website = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Project(models.Model):
    PROJECT_TYPES = [
        ("software", "Software"),
        ("solar", "Solar"),
        ("iot", "IoT"),
        ("research", "Research"),
        ("opensource", "Open Source"),
        ("strategy", "Strategic Design"),
    ]

    title = models.CharField(max_length=160)
    slug = models.SlugField(unique=True)
    project_type = models.CharField(max_length=40, choices=PROJECT_TYPES)
    summary = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to="projects/", blank=True)
    client = models.CharField(max_length=140, blank=True)
    location = models.CharField(max_length=140, blank=True)
    year = models.PositiveIntegerField(null=True, blank=True)
    technologies = models.TextField(blank=True, help_text="One technology per line")
    outcome = models.TextField(blank=True)
    is_featured = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-year", "title"]

    def __str__(self):
        return self.title

    def technology_list(self):
        return _lines(self.technologies)


class JobOpening(models.Model):
    EMPLOYMENT_TYPES = [
        ("full_time", "Full-Time"),
        ("part_time", "Part-Time"),
        ("contract", "Contract"),
        ("internship", "Internship"),
        ("volunteer", "Volunteer"),
    ]

    title = models.CharField(max_length=160)
    slug = models.SlugField(unique=True)
    location = models.CharField(max_length=140, default="Nairobi")
    employment_type = models.CharField(max_length=40, choices=EMPLOYMENT_TYPES, default="full_time")
    summary = models.TextField()
    responsibilities = models.TextField(help_text="One responsibility per line")
    requirements = models.TextField(help_text="One requirement per line")
    closing_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    notify_subscribers = models.BooleanField(default=True)
    notification_sent = models.BooleanField(default=False, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("career_detail", kwargs={"slug": self.slug})

    def responsibility_list(self):
        return _lines(self.responsibilities)

    def requirement_list(self):
        return _lines(self.requirements)


class JobApplication(models.Model):
    job = models.ForeignKey(JobOpening, related_name="applications", on_delete=models.CASCADE)
    full_name = models.CharField(max_length=140)
    email = models.EmailField()
    phone = models.CharField(max_length=60, blank=True)
    cover_letter = models.TextField()
    cv = models.FileField(upload_to="applications/cv/")
    portfolio = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    reviewed = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.full_name} - {self.job.title}"


class OutreachEvent(models.Model):
    title = models.CharField(max_length=160)
    slug = models.SlugField(unique=True)
    summary = models.TextField()
    description = models.TextField()
    program_type = models.CharField(max_length=120, blank=True)
    location = models.CharField(max_length=140, blank=True)
    event_date = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to="outreach/", blank=True)
    is_published = models.BooleanField(default=True)
    notify_subscribers = models.BooleanField(default=True)
    notification_sent = models.BooleanField(default=False, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-event_date", "-created_at"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("outreach")


class MentorshipCohort(models.Model):
    TRACKS = [
        ("software", "Software Engineering"),
        ("energy", "Renewable Energy"),
        ("design", "Strategic Design"),
    ]

    title = models.CharField(max_length=160)
    slug = models.SlugField(unique=True)
    track = models.CharField(max_length=40, choices=TRACKS)
    summary = models.TextField()
    description = models.TextField()
    start_date = models.DateField(null=True, blank=True)
    application_deadline = models.DateField(null=True, blank=True)
    is_open = models.BooleanField(default=True)
    notify_subscribers = models.BooleanField(default=True)
    notification_sent = models.BooleanField(default=False, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("mentorship")


class MentorshipRegistration(models.Model):
    cohort = models.ForeignKey(MentorshipCohort, related_name="registrations", on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=140)
    email = models.EmailField()
    university_or_organization = models.CharField(max_length=180)
    interests = models.TextField()
    experience = models.TextField()
    goals = models.TextField()
    resume = models.FileField(upload_to="mentorship/resumes/", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    reviewed = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    name = models.CharField(max_length=120)
    role = models.CharField(max_length=140, blank=True)
    quote = models.TextField()
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class PricingPlan(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=80)
    description = models.TextField()
    features = models.TextField(help_text="One feature per line")
    is_featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "name"]

    def __str__(self):
        return self.name

    def feature_list(self):
        return _lines(self.features)


def _lines(value):
    return [line.strip() for line in value.splitlines() if line.strip()]
