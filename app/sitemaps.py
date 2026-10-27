from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = "weekly"

    def items(self):
        return [
            "Home", "products", "BabyCot", "ClassicRanges", "SkinRanges", "VeneerRanges",
            "LaminateRanges", "LightOpeningRanges", "Furnitureforkids", "Tvunit", "Wardrobe",
            "seasoningchamber", "Corporate", "careers", "contact",
        ]

    def location(self, item):
        return reverse(item)
