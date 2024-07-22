from django.db import models
from wagtail.models import Page, Collection, Orderable
from wagtail.fields import StreamField, RichTextField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.snippets.models import register_snippet
from wagtail.documents.models import Document
from modelcluster.fields import ParentalKey

from .blocks import DescriptionBlock


class AccomodationPage(Page):
    image = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="+",
    )

    introduction_title = models.CharField(
        max_length=255,
        default="Accommodation",
        help_text="Title displayed above the introductory text",
        blank=True,
        null=True,
    )
    introduction_text = RichTextField(
        features=["bold", "italic", "link"],
        help_text="Introductory text about the accommodation options",
        blank=True,
        null=True,
    )

    feature_description_one = StreamField(
        DescriptionBlock(), use_json_field=True, blank=True, null=True
    )
    feature_description_two = StreamField(
        DescriptionBlock(), use_json_field=True, blank=True, null=True
    )

    cta_button_text = models.CharField(
        max_length=255,
        default="Prices & Availability",
        help_text="Text for the call to action button",
        blank=True,
        null=True,
    )
    cta_button_link = models.ForeignKey(
        "wagtailcore.Page",
        related_name="+",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    image_collection_one = models.ForeignKey(
        Collection,
        limit_choices_to=~models.Q(name__in=["Root"]),
        null=True,
        related_name="+",
        blank=True,
        on_delete=models.SET_NULL,
        help_text="Select the image collection for this gallery.",
    )

    look_around_title = models.CharField(
        max_length=255,
        help_text="Title for Take a look around section",
        blank=True,
        null=True,
        default="Take a look around...",
    )
    look_around_text = RichTextField(
        help_text="Text for Take a look around section",
        blank=True,
        features=["bold", "italic", "link"],
    )

    cta_button_text_two = models.CharField(
        max_length=255,
        default="DOWNLOAD FLOOR LAYOUT",
        help_text="Text for this button",
        blank=True,
        null=True,
    )

    floor_layout_doc = models.ForeignKey(
        Document,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Select the floor layout document.",
    )

    image_collection_two = models.ForeignKey(
        Collection,
        limit_choices_to=~models.Q(name__in=["Root"]),
        null=True,
        related_name="+",
        blank=True,
        on_delete=models.SET_NULL,
        help_text="Select the image collection for this gallery.",
    )

    retreat_facility = models.ForeignKey(
        "RoomType", on_delete=models.SET_NULL, null=True, blank=True, related_name="+"
    )
    classic_room = models.ForeignKey(
        "RoomType", on_delete=models.SET_NULL, null=True, blank=True, related_name="+"
    )

    upper_level_room = models.ForeignKey(
        "RoomType",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="+",
    )
    family_suite = models.ForeignKey(
        "RoomType",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="+",
    )
    deluxe_suite = models.ForeignKey(
        "RoomType",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="+",
    )

    content_panels = Page.content_panels + [
        FieldPanel("image"),
        MultiFieldPanel(
            [
                FieldPanel("introduction_title"),
                FieldPanel("introduction_text"),
            ],
            heading="Introduction",
        ),
        MultiFieldPanel(
            [
                FieldPanel("feature_description_one"),
                FieldPanel("feature_description_two"),
                MultiFieldPanel(
                    [
                        FieldPanel("cta_button_text"),
                        FieldPanel("cta_button_link"),
                    ],
                    heading="CTA Button",
                ),
            ],
            heading="Description",
        ),
        FieldPanel("image_collection_one"),
        MultiFieldPanel(
            [
                FieldPanel("look_around_title"),
                FieldPanel("look_around_text"),
                FieldPanel("image_collection_two"),
            ],
            heading="Look Around Section",
        ),
        MultiFieldPanel(
            [
                FieldPanel("floor_layout_doc"),
                FieldPanel("cta_button_text_two"),
            ],
            heading="Floor Layout Document",
        ),
        MultiFieldPanel(
            [
                FieldPanel("retreat_facility"),
                FieldPanel("upper_level_room"),
                FieldPanel("family_suite"),
                FieldPanel("deluxe_suite"),
                FieldPanel("classic_room"),
            ],
            heading="Rooms",
        ),
    ]


@register_snippet
class RoomType(models.Model):
    """Snippet to define details of a specific room type."""

    name = models.CharField(max_length=255)
    description = RichTextField()
    cta_text = models.CharField(
        max_length=255,
        default="REQUEST TO BOOK",
        help_text="Text for the call to action button",
        blank=True,
        null=True,
    )
    cta_link = models.ForeignKey(
        "wagtailcore.Page",
        related_name="+",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    # gallery = models.ForeignKey(
    #     Collection,
    #     limit_choices_to=~models.Q(name__in=["Root"]),
    #     null=True,
    #     related_name="+",
    #     blank=True,
    #     on_delete=models.SET_NULL,
    #     help_text="Select the image collection for this gallery.",
    # )
    image = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="+",
    )


    panels = [
        FieldPanel("name"),
        FieldPanel("description"),
        FieldPanel("image"),
        MultiFieldPanel(
            [
                FieldPanel("cta_text"),
                FieldPanel("cta_link"),
            ],
            heading="CTA Button",
        ),
    ]

    def __str__(self):
        return self.name


@register_snippet
class RoomNumber(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    cleaning_charge = models.DecimalField(max_digits=10, decimal_places=2)

    panels = [
        FieldPanel("name"),
        FieldPanel("description"),
        FieldPanel("cleaning_charge"),
    ]

    def __str__(self):
        return self.name


@register_snippet
class Availability(models.Model):
    STATUS_CHOICES = [
        ("available", "Available"),
        ("booked", "Booked"),
        ("changeover", "Changeover"),
        ("pending", "Pending"),
    ]

    room_number = models.ForeignKey(
        RoomNumber, on_delete=models.CASCADE, related_name="availabilities",null=True
    )
    date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    panels = [
        FieldPanel("room_number"),
        FieldPanel("date"),
        FieldPanel("status"),
    ]

    def __str__(self):
        return f"{self.room_number.name} - {self.date} - {self.status}"


@register_snippet
class Pricing(models.Model):
    DURATION_CHOICES = [
        ("2_night", "2 Night"),
        ("3_night", "3 Night"),
        ("4_night", "4 Night"),
        ("5_night", "5 Night"),
        ("6_night", "6 Night"),
        ("7_night", "7 Night"),
    ]

    MONTH_CHOICES = [
        ("january_february", "January | February"),
        ("march_april", "March | April"),
        ("may_june", "May | June"),
        ("july_august", "July | August"),
        ("september_october", "September | October"),
        ("november_december", "November | December"),
    ]

    room_number = models.ForeignKey(
        RoomNumber, on_delete=models.CASCADE, related_name="pricing"
    )
    month = models.CharField(max_length=20, choices=MONTH_CHOICES)
    duration = models.CharField(max_length=10, choices=DURATION_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    panels = [
        FieldPanel("room_number"),
        FieldPanel("month"),
        FieldPanel("duration"),
        FieldPanel("price"),
    ]

    def __str__(self):
        return (
            f"{self.room_number.name} - {self.month} - {self.duration} - {self.price}"
        )


class AvailabilityPricesPage(Page):
    image = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="+",
    )

    introduction_text = RichTextField(
        features=["bold", "italic", "link"],
        help_text="Introductory text about the accommodation options",
        blank=True,
        null=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("image"),
        FieldPanel("introduction_text"),
        MultiFieldPanel(
            [InlinePanel("room_numbers", label="Room Types")],
            heading="Room Types",
        ),
        MultiFieldPanel(
            [InlinePanel("availabilities", label="Availabilities")],
            heading="Availabilities",
        ),
        MultiFieldPanel(
            [InlinePanel("pricing", label="Pricing")],
            heading="Pricing",
        ),
    ]


class RoomNumberOrderable(Orderable, models.Model):
    page = ParentalKey(
        AvailabilityPricesPage, on_delete=models.CASCADE, related_name="room_numbers"
    )
    room_number = models.ForeignKey(
        RoomNumber, on_delete=models.CASCADE, related_name="+"
    )

    panels = [FieldPanel("room_number")]


class AvailabilityOrderable(Orderable, models.Model):
    page = ParentalKey(
        AvailabilityPricesPage, on_delete=models.CASCADE, related_name="availabilities"
    )
    availability = models.ForeignKey(
        Availability, on_delete=models.CASCADE, related_name="+"
    )

    panels = [FieldPanel("availability")]


class PricingOrderable(Orderable, models.Model):
    page = ParentalKey(
        AvailabilityPricesPage, on_delete=models.CASCADE, related_name="pricing"
    )
    pricing = models.ForeignKey(Pricing, on_delete=models.CASCADE, related_name="+")

    panels = [FieldPanel("pricing")]

class GroupsPage(Page):
    pass