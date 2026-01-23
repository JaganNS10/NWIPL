from django.db import models

class Job(models.Model):

    JOB_TYPE_CHOICES = [
        ('Full Time', 'Full Time'),
    ]

    title = models.CharField(max_length=200)
    department = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    experience_required = models.CharField(max_length=50)
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    posted_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
class JobApplication(models.Model):

    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=15)

    year_of_graduation = models.PositiveIntegerField()

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    experience_years = models.DecimalField(max_digits=3, decimal_places=1)

    current_employer = models.CharField(max_length=200, blank=True)

    current_ctc = models.DecimalField(max_digits=5, decimal_places=2)
    expected_ctc = models.DecimalField(max_digits=5, decimal_places=2)

    NOTICE_PERIOD_CHOICES = [
        ('Immediate', 'Immediate'),
        ('15 Days', '15 Days'),
        ('30 Days', '30 Days'),
        ('60 Days', '60 Days'),
        ('90 Days', '90 Days'),
    ]
    notice_period = models.CharField(max_length=20, choices=NOTICE_PERIOD_CHOICES)


    current_location = models.CharField(max_length=100)

    resume = models.FileField(upload_to='resumes/')

    applied_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} - {self.job.title}"
