from django.db import models

from wagtail.contrib.settings.models import register_setting, BaseSiteSetting
from wagtail.admin.panels import FieldPanel

@register_setting
class SiteSettings(BaseSiteSetting):
    title_suffix = models.CharField(
        verbose_name="Title Suffix", max_length=255, default="Villarosa"
    )

    panels = [FieldPanel("title_suffix")]
