from django.urls import path

from . import views

urlpatterns = [
    path("", views.Home, name="Home"),
    path("products/", views.products, name="products"),
    path("BabyCot/", views.BabyCot, name="BabyCot"),
    path("ClassicRanges/", views.ClassicRanges, name="ClassicRanges"),
    path("SkinRanges/", views.SkinRanges, name="SkinRanges"),
    path("VeneerRanges/", views.VeneerRanges, name="VeneerRanges"),
    path("LaminateRanges/", views.LaminateRanges, name="LaminateRanges"),
    path("LightOpeningRanges/", views.LightOpeningRanges, name="LightOpeningRanges"),
    path("Furnitureforkids/", views.Furnitureforkids, name="Furnitureforkids"),
    path("Tvunit/", views.Tvunit, name="Tvunit"),
    path("Wardrobe/", views.Wardrobe, name="Wardrobe"),
    path("Corporate/", views.Corporate, name="Corporate"),
    path("seasoningchamber/", views.seasoningchamber, name="seasoningchamber"),
    path("careers/", views.careers, name="careers"),
    path("job_detail/<int:id>/", views.job_detail, name="job_detail"),
    path("job_apply/<int:id>/", views.job_apply, name="job_apply"),
    path("contact/", views.contact, name="contact"),
    path("contact/thanks/", views.contact_thanks, name="contact_thanks"),
]
