from django import forms

from .models import JobApplication, MentorshipRegistration


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ["full_name", "email", "phone", "cover_letter", "cv", "portfolio", "linkedin", "github"]
        widgets = {
            "cover_letter": forms.Textarea(attrs={"rows": 5}),
        }


class MentorshipRegistrationForm(forms.ModelForm):
    class Meta:
        model = MentorshipRegistration
        fields = [
            "cohort",
            "name",
            "email",
            "university_or_organization",
            "interests",
            "experience",
            "goals",
            "resume",
        ]
        widgets = {
            "interests": forms.Textarea(attrs={"rows": 3}),
            "experience": forms.Textarea(attrs={"rows": 3}),
            "goals": forms.Textarea(attrs={"rows": 4}),
        }
