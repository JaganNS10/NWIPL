from django.contrib import admin

from .models import BabyCotModel, Enquiry, Job, JobApplication


@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ("created_at", "name", "phone", "enquiry_type", "source", "email_sent", "is_handled")
    list_filter = ("enquiry_type", "is_handled", "email_sent")
    list_editable = ("is_handled",)
    search_fields = ("name", "phone", "email", "message", "source")
    readonly_fields = ("created_at", "email_sent")


@admin.register(BabyCotModel)
class BabyCotModelAdmin(admin.ModelAdmin):
    list_display = ("code", "variant", "position", "is_active")
    list_editable = ("position", "is_active")


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ("title", "department", "location", "is_active", "posted_on")
    list_filter = ("is_active", "department")


@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "job", "email", "contact", "applied_on")
    list_filter = ("job",)
    search_fields = ("first_name", "last_name", "email", "contact")
