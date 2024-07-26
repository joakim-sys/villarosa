from django.db import models

from wagtail.models import Page

from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.fields import StreamField
from modelcluster.fields import ParentalKey
from .blocks import Carousel, PostStreamBlock, AccomodationBody, ImageStream


class HomePage(Page):
    carousel = StreamField(
        Carousel(),
        use_json_field=True,
        blank=True,
        null=True,
    )

    introduction_title = models.CharField(
        "Main Heading",
        max_length=255,
        null=True,
        blank=True,
        help_text="Enter the primary headline for the homepage introduction",
    )
    introduction_subheading = models.TextField(
        "Subheading",
        null=True,
        blank=True,
        help_text="Provide a brief description or tagline to appear below the main heading.",
    )
    introduction_cta_text = models.CharField(
        "Call to Action Button Text",
        help_text="Enter the text you want to display on the call-to-action button (e.g., 'Learn More', 'Book Now",
        max_length=255,
        null=True,
        blank=True,
    )
    introduction_cta_link = models.ForeignKey(
        "wagtailcore.Page",
        related_name="+",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="Call to Action Button Link",
    )

    featured_section_one = StreamField(
        PostStreamBlock(), use_json_field=True, null=True, blank=True, help_text=""
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
            heading="Homepage Carousel",
            help_text="Upload images to display in a rotating carousel at the top of the homepage. Recommended image dimensions: 1920px width x 1080px height.",
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
                FieldPanel(
                    "featured_section_one",
                    heading="Featured Retreat Category 1",
                    help_text="Choose retreats to highlight in this section. Example categories: 'Family Getaways', 'Romantic Escapes', 'Wellness Retreats",
                ),
                FieldPanel(
                    "featured_section_two",
                    heading="Featured Retreat Category 2",
                    help_text="Choose retreats to highlight in this section. Example categories: 'Adventure Packages', 'Group Specials', 'Last-Minute Deals",
                ),
            ],
            heading="Featured Categories",
        ),
        FieldPanel(
            "section_three",
            heading="Special Offer Text",
            help_text="Enter text to highlight a special offer or promotion (e.g., 'View Our Latest Packages').",
        ),
        MultiFieldPanel(
            [
                FieldPanel("accomodation_section_title", heading="Highlights Title"),
                FieldPanel("accomodation_section_subheading"),
                FieldPanel(
                    "accommodation_section_image",
                    heading="Featured Image",
                    help_text="",
                ),
                InlinePanel(
                    "acc_features",
                    label="Highlights",
                    help_text="Use bullet points, short phrases, or icons to showcase key features, benefits, or information.",
                ),
                FieldPanel(
                    "accomodation_section_paragraph",
                ),
                FieldPanel(
                    "accomodation_section_cta_link",
                    heading="Call to Action Button Link",
                ),
            ],
            heading="Featured Image & Highlights ",
            help_text="This section uses a split-screen layout, ideal for visually presenting key features or selling points. One side prominently features an image, while the other uses concise text, bullet points, or icons.",
        ),
        MultiFieldPanel(
            [
                FieldPanel("location_section_title", heading="Showcase Title"),
                FieldPanel(
                    "location_section_subheading", heading="Showcase Subheading"
                ),
                InlinePanel(
                    "locations",
                    max_num=2,
                    heading="Showcase Items",
                    help_text="Add content for each item you want to feature in the two-column grid",
                ),
            ],
            heading="Two-Column Showcase",
            help_text="This section employs a two-column grid to present content in a visually balanced way. Perfect for showcasing multiple locations, activities, services, or categories with images and descriptions.",
        ),
        MultiFieldPanel(
            [FieldPanel("services_section_title"), InlinePanel("services", max_num=3)],
            heading="Three-Up Feature Grid",
            help_text="This section utilizes a three-column grid to highlight additional options, services, or categories in a concise and scannable format. Each item typically includes an image and a short description.",
        ),
        # MultiFieldPanel(
        #     [InlinePanel("icon_links", max_num=6)],
        #     heading="Icon Links Section",
        # ),
        MultiFieldPanel(
            [
                FieldPanel(
                    "styled_link_text",
                    heading="Special Offer Text",
                    help_text="Enter text to highlight a special offer or promotion (e.g., 'View Our Latest Packages').",
                ),
                FieldPanel(
                    "styled_link_text_link",
                    heading="Special Offer Link",
                    help_text="Select the page where users can find more details about the offer.",
                ),
            ],
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

    name = models.CharField(
        "Item Title",
        max_length=255,
        help_text="Provide a short, descriptive title for this item",
    )
    text = models.TextField(
        "Item Description",
        null=True,
        blank=True,
        help_text="Add a brief description of the item",
    )

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"


class AccomodationFeature(models.Model):
    name = models.CharField(max_length=255)
    page = ParentalKey(
        "HomePage", related_name="acc_features", on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Feauture"
        verbose_name_plural = "Features"
