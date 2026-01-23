from .models import JobApplication
from django import forms


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['first_name', 'last_name', 'email', 'contact',
                  'year_of_graduation', 'gender', 'experience_years',
                  'current_employer', 'current_ctc', 'expected_ctc','notice_period','current_location', 'resume']