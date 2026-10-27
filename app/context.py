from django.templatetags.static import static


def site(request):
    """Business details used in the footer, contact section and structured data."""
    return {
        "SITE": {
            "name": "Neminath Wood Industry (P) Ltd",
            "phone": "+91 81225 07384",
            "phone_link": "+918122507384",
            "email": "neminathwoodindustry.pvt.ltd@gmail.com",
            "address": "Chennai, Tamil Nadu, India",
            "brochure": static("downloads/NeminathProfileBrochure.pdf"),
        }
    }
