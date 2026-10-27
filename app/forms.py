import re

from django import forms

from .models import Enquiry, JobApplication


class EnquiryForm(forms.ModelForm):
    # Honeypot: real visitors never see or fill this field, bots usually do.
    website = forms.CharField(required=False, widget=forms.TextInput(attrs={
        "tabindex": "-1", "autocomplete": "off", "aria-hidden": "true",
    }))

    class Meta:
        model = Enquiry
        fields = ["name", "phone", "email", "enquiry_type", "message", "source"]
        widgets = {
            "name": forms.TextInput(attrs={"autocomplete": "name", "placeholder": "Your name"}),
            "phone": forms.TextInput(attrs={"autocomplete": "tel", "inputmode": "tel", "placeholder": "Phone number"}),
            "email": forms.EmailInput(attrs={"autocomplete": "email", "placeholder": "Email (optional)"}),
            "message": forms.Textarea(attrs={"rows": 4, "placeholder": "Tell us what you need"}),
            "source": forms.HiddenInput(),
        }
        labels = {"name": "Name", "phone": "Phone", "email": "Email", "enquiry_type": "I am enquiring", "message": "Message"}

    def clean_phone(self):
        phone = self.cleaned_data["phone"].strip()
        digits = re.sub(r"\D", "", phone)
        if not re.fullmatch(r"[+\d\s()\-]+", phone) or not 7 <= len(digits) <= 15:
            raise forms.ValidationError("Please enter a valid phone number.")
        return phone

    def clean_website(self):
        if self.cleaned_data.get("website"):
            raise forms.ValidationError("Spam detected.")
        return ""


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = [
            "first_name", "last_name", "email", "contact", "year_of_graduation", "gender",
            "experience_years", "current_employer", "current_ctc", "expected_ctc",
            "notice_period", "current_location", "resume",
        ]

    def clean_resume(self):
        f = self.cleaned_data["resume"]
        if f.size > 5 * 1024 * 1024:
            raise forms.ValidationError("Resume must be 5 MB or smaller.")
        if not f.name.lower().endswith((".pdf", ".doc", ".docx")):
            raise forms.ValidationError("Please upload a PDF or Word file.")
        return f
