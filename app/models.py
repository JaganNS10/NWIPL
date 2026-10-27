from django.db import models


class Job(models.Model):
    JOB_TYPE_CHOICES = [("Full Time", "Full Time")]

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
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="applications")

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=15)

    year_of_graduation = models.PositiveIntegerField()

    GENDER_CHOICES = [("Male", "Male"), ("Female", "Female"), ("Other", "Other")]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    experience_years = models.DecimalField(max_digits=3, decimal_places=1)
    current_employer = models.CharField(max_length=200, blank=True)
    current_ctc = models.DecimalField(max_digits=5, decimal_places=2)
    expected_ctc = models.DecimalField(max_digits=5, decimal_places=2)

    NOTICE_PERIOD_CHOICES = [
        ("Immediate", "Immediate"),
        ("15 Days", "15 Days"),
        ("30 Days", "30 Days"),
        ("60 Days", "60 Days"),
        ("90 Days", "90 Days"),
    ]
    notice_period = models.CharField(max_length=20, choices=NOTICE_PERIOD_CHOICES)
    current_location = models.CharField(max_length=100)
    resume = models.FileField(upload_to="resumes/")
    applied_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} - {self.job.title}"


class Enquiry(models.Model):
    """Every message sent from the website's enquiry form is stored here."""

    TYPE_CHOICES = [
        ("home", "For my home"),
        ("project", "Builder / project"),
        ("other", "Something else"),
    ]

    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    enquiry_type = models.CharField(max_length=10, choices=TYPE_CHOICES, default="home")
    message = models.TextField(blank=True)
    source = models.CharField("Enquired about", max_length=120, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    email_sent = models.BooleanField(default=False)
    is_handled = models.BooleanField("Handled", default=False)

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "enquiries"

    def __str__(self):
        return f"{self.name} ({self.created_at:%d %b %Y})"


class BabyCotModel(models.Model):
    """One model on the Baby Cot page. Add or edit these in /admin/."""

    code = models.CharField(max_length=40, unique=True)
    description = models.TextField()
    material = models.CharField(max_length=120)
    finish = models.CharField(max_length=120)
    joinery = models.CharField(max_length=120, default="Dowel & barrel-nut construction")
    variant = models.CharField(max_length=120)
    image = models.CharField(
        max_length=200,
        help_text="Path inside static/, for example images/BabyCot/nwibc1a01.jpeg",
    )
    position = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["position", "id"]
        verbose_name = "baby cot model"

    def __str__(self):
        return self.code
