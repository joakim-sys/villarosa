from django.db import models

from wagtail.models import Page

from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.fields import StreamField
from modelcluster.fields import ParentalKey
from .blocks import Carousel, PostStreamBlock, AccomodationBody, ImageStream


class HomePage(Page):
    carousel = StreamField(Carousel(), use_json_field=True, blank=True, null=True)

    introduction_title = models.CharField(max_length=255, null=True, blank=True)
    introduction_subheading = models.TextField(null=True, blank=True)
    introduction_cta_text = models.CharField(max_length=255, null=True, blank=True)
    introduction_cta_link = models.ForeignKey(
        "wagtailcore.Page",
        related_name="+",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    featured_section_one = StreamField(
        PostStreamBlock(), use_json_field=True, null=True, blank=True
    )
    featured_section_two = StreamField(
        PostStreamBlock(), use_json_field=True, null=True, blank=True
    )

    section_three = models.CharField(max_length=255, null=True, blank=True)
    accomodation_section_title = models.CharField(max_length=255, null=True, blank=True)
    accomodation_section_subheading = models.TextField(null=True, blank=True)
    accomodation_section_paragraph = models.TextField(null=True, blank=True)
    accomodation_section_cta_link = models.ForeignKey(
        "wagtailcore.Page",
        related_name="+",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    location_section_title = models.CharField(max_length=255, null=True, blank=True)
    location_section_subheading = models.TextField(null=True, blank=True)

    services_section_title = models.CharField(max_length=255, null=True, blank=True)

    styled_link_text = models.CharField(max_length=256, null=True, blank=True)
    styled_link_text_link = models.ForeignKey(
        "wagtailcore.Page",
        related_name="+",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    accommodation_section_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
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
        MultiFieldPanel(
            [
                FieldPanel("featured_section_one"),
                FieldPanel("featured_section_two"),
            ],
            heading="Featured Pages",
        ),
        FieldPanel("section_three"),
        MultiFieldPanel(
            [
                FieldPanel("accomodation_section_title"),
                FieldPanel("accomodation_section_subheading"),
                FieldPanel("accommodation_section_image"),
                InlinePanel("acc_features", label="Feature"),
                FieldPanel("accomodation_section_paragraph"),
                FieldPanel("accomodation_section_cta_link"),
            ],
            heading="Accomodation Section",
        ),
        MultiFieldPanel(
            [
                FieldPanel("location_section_title"),
                FieldPanel("location_section_subheading"),
                InlinePanel("locations", max_num=2),
            ],
            heading="Location Section",
        ),
        MultiFieldPanel(
            [FieldPanel("services_section_title"), InlinePanel("services", max_num=3)],
            heading="Services Section",
        ),
        # MultiFieldPanel(
        #     [InlinePanel("icon_links", max_num=6)],
        #     heading="Icon Links Section",
        # ),
        MultiFieldPanel(
            [FieldPanel("styled_link_text"), FieldPanel("styled_link_text_link")],
            heading="Styled Link Section",
        ),
    ]


class Service(models.Model):
    page = ParentalKey("HomePage", related_name="services", on_delete=models.CASCADE)
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    name = models.CharField(max_length=255)
    text = models.TextField(null=True, blank=True)
    cta_text = models.CharField(max_length=255, null=True)
    cta_link = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )


class IconLink(models.Model):
    title = models.CharField(max_length=255, null=True)
    icon = models.CharField(
        max_length=255,
        choices=[
            ("e_fas_swimmer", "Swimmer"),
            ("e_fas_biking", "Biking"),
            ("e_fas_car_alt", "Car"),
            ("e_fas_bus", "Bus"),
            ("e_fas_glass_cheers", "Glass Cheers"),
            ("e_fas_atom", "Atom"),
        ],
    )
    link = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    page = ParentalKey("HomePage", related_name="icon_links", on_delete=models.CASCADE)


class Location(models.Model):
    page = ParentalKey("HomePage", related_name="locations", on_delete=models.CASCADE)
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    name = models.CharField(max_length=255)
    text = models.TextField(null=True, blank=True)


class AccomodationFeature(models.Model):
    name = models.CharField(max_length=255)
    page = ParentalKey(
        "HomePage", related_name="acc_features", on_delete=models.CASCADE
    )
