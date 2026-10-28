from django.contrib import admin
from django.core.exceptions import PermissionDenied
from django.urls import path

from .exports import enquiries_excel_response
from .models import BabyCotModel, Enquiry, Job, JobApplication


@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ("created_at", "name", "phone", "enquiry_type", "source", "email_sent", "is_handled")
    list_filter = ("enquiry_type", "is_handled", "email_sent")
    list_editable = ("is_handled",)
    search_fields = ("name", "phone", "email", "message", "source")
    readonly_fields = ("created_at", "email_sent")
    date_hierarchy = "created_at"
    actions = ["download_excel"]

    def get_urls(self):
        custom = [path("export-excel/", self.admin_site.admin_view(self.export_excel), name="app_enquiry_export")]
        return custom + super().get_urls()

    def export_excel(self, request):
        """The 'Download Excel' button: exports whatever the list is currently showing (filters, dates, search)."""
        if not self.has_view_permission(request):
            raise PermissionDenied
        queryset = self.get_changelist_instance(request).get_queryset(request)
        return enquiries_excel_response(queryset)

    @admin.action(description="Download selected enquiries as Excel")
    def download_excel(self, request, queryset):
        return enquiries_excel_response(queryset)


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
