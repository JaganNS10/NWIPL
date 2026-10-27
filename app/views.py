import logging

from django.contrib import messages
from django.core.cache import cache
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.http import url_has_allowed_host_and_scheme

from . import catalog
from .forms import EnquiryForm, JobApplicationForm
from .mailer import send_brevo_email
from .models import BabyCotModel, Enquiry, Job

log = logging.getLogger(__name__)


def _enquiry_form(request):
    """Blank enquiry form, pre-filled when a page links here with ?ref=<product>."""
    ref = request.GET.get("ref", "").strip()[:100]
    initial = {"source": ref}
    if ref:
        initial["message"] = f"I would like to enquire about: {ref}"
    return EnquiryForm(initial=initial)


def Home(request):
    return render(request, "index.html", {
        "hero_slides": catalog.HERO_SLIDES,
        "tiles": catalog.SHOP_TILES,
        "collections": catalog.COLLECTIONS,
        "clients": catalog.CLIENTS,
        "form": _enquiry_form(request),
    })


def products(request):
    return render(request, "products.html", {
        "features": catalog.PRODUCT_FEATURES,
        "gallery": catalog.PRODUCT_GALLERY,
        "collections": catalog.COLLECTIONS,
    })


def BabyCot(request):
    return render(request, "BabyCot.html", {
        "intro": catalog.BABYCOT_INTRO,
        "models": BabyCotModel.objects.filter(is_active=True),
    })


def ClassicRanges(request):
    return render(request, "ClassicRanges.html", {"r": catalog.RANGES["classic"]})


def SkinRanges(request):
    return render(request, "SkinRanges.html", {"r": catalog.RANGES["skin"]})


def VeneerRanges(request):
    return render(request, "VeneerRanges.html", {"r": catalog.RANGES["veneer"]})


def LaminateRanges(request):
    return render(request, "LaminateRanges.html", {"r": catalog.RANGES["laminate"]})


def LightOpeningRanges(request):
    return render(request, "LightOpeningRanges.html", {"r": catalog.RANGES["light"]})


def Wardrobe(request):
    return render(request, "Wardrobe.html", {"s": catalog.SPACES["wardrobe"]})


def Tvunit(request):
    return render(request, "TVUnit.html", {"s": catalog.SPACES["tv"]})


def Furnitureforkids(request):
    return render(request, "FurnitureforKids.html", {"s": catalog.SPACES["kids"]})


def Corporate(request):
    return render(request, "Corporate.html", {"s": catalog.SPACES["corporate"], "clients": catalog.CLIENTS})


def seasoningchamber(request):
    return render(request, "seasoningchamber.html", {"d": catalog.SEASONING})


# ---------- Careers ----------

def careers(request):
    jobs = Job.objects.filter(is_active=True)
    return render(request, "careers.html", {"jobs": jobs})


def job_detail(request, id):
    job = get_object_or_404(Job, id=id, is_active=True)
    return render(request, "job_detail.html", {"job": job})


def job_apply(request, id):
    job = get_object_or_404(Job, id=id, is_active=True)
    if request.method == "POST":
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.save()

            name = f"{form.cleaned_data['first_name']} {form.cleaned_data['last_name']}"
            send_brevo_email(
                form.cleaned_data["email"],
                "Application Received – Neminath Wood Industry Pvt Ltd",
                f"Hi {name},\n\nThank you for your interest in Neminath Wood Industry Private Limited.\n"
                f"We have successfully received your application for the position of {job.title}.\n\n"
                "Our team will contact you if your profile matches the required position.\n\n"
                "Best regards,\nTalent Acquisition Team\nNeminath Wood Industry Pvt Ltd",
            )
            resume = request.FILES["resume"]
            resume.seek(0)  # the file was read while saving; rewind so the attachment is not empty
            send_brevo_email(
                "hr@nwipl.com",
                f"Job Application from {name}",
                f"{name} has applied for {job.title}.\n"
                f"Email: {form.cleaned_data['email']}\nContact: {form.cleaned_data['contact']}\n",
                attachment=resume.read(),
                attachment_name=resume.name,
                reply_to=form.cleaned_data["email"],
            )
            messages.success(
                request,
                f"Your application for {job.title} has been submitted successfully. Check your email for confirmation.",
            )
            return redirect("careers")
        messages.error(request, "Please correct the highlighted fields and try again.")
    else:
        form = JobApplicationForm()
    return render(request, "job_apply.html", {"job": job, "form": form})


# ---------- Enquiries ----------

def _client_ip(request):
    forwarded = request.META.get("HTTP_X_FORWARDED_FOR", "")
    return (forwarded.split(",")[0].strip() if forwarded else request.META.get("REMOTE_ADDR", "")) or "unknown"


def _notify(enquiry):
    body = (
        f"New enquiry from the website\n\n"
        f"Name: {enquiry.name}\nPhone: {enquiry.phone}\nEmail: {enquiry.email or '-'}\n"
        f"Type: {enquiry.get_enquiry_type_display()}\nAbout: {enquiry.source or '-'}\n\n"
        f"Message:\n{enquiry.message or '-'}\n"
    )
    from django.conf import settings
    ok = send_brevo_email(
        settings.ENQUIRY_TO_EMAIL,
        f"New website enquiry from {enquiry.name}",
        body,
        reply_to=enquiry.email or None,
    )
    if ok:
        Enquiry.objects.filter(pk=enquiry.pk).update(email_sent=True)


def contact(request):
    if request.method != "POST":
        return render(request, "contact.html", {"form": _enquiry_form(request)})

    form = EnquiryForm(request.POST)
    key = f"enquiry:{_client_ip(request)}"
    if cache.get(key, 0) >= 5:
        messages.error(request, "Too many enquiries from this connection. Please try again in an hour.")
        return render(request, "contact.html", {"form": form}, status=429)

    if form.is_valid():
        enquiry = form.save()
        cache.set(key, cache.get(key, 0) + 1, 3600)
        _notify(enquiry)
        return redirect("contact_thanks")
    return render(request, "contact.html", {"form": form}, status=400)


def contact_thanks(request):
    return render(request, "thanks.html")


def not_found(request, exception=None):
    return render(request, "404.html", status=404)
