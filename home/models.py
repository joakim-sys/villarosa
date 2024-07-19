from django.db import models

from wagtail.models import Page

from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.fields import StreamField
from .blocks import Carousel


class HomePage(Page):
    carousel = StreamField(Carousel(), use_json_field=True, blank=True, null=True)

    introduction_title = models.CharField(max_length=255, null=True, blank=True)
    introduction_subheading = models.TextField(null=True, blank=True)
    introduction_cta_text = models.CharField(
        max_length=255, null=True, blank=True
    )
    introduction_cta_link = models.ForeignKey(
        "wagtailcore.Page",
        related_name="+",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("carousel"),
            ],
            heading="Carousel Section",
        ),
        MultiFieldPanel(
            [
                FieldPanel("introduction_title"),
                FieldPanel("introduction_subheading"),
                FieldPanel("introduction_cta_text"),
                FieldPanel("introduction_cta_link"),
            ],
            heading="Introduction Section",
        ),
    ]
