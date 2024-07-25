from django.db import models
from wagtail.models import Page, Collection
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, FieldRowPanel


# Groups Page
class PageTwo(Page):
    image = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="+",
    )

    introduction = models.TextField()
    section_one_body_left = RichTextField(
        features=["bold", "italic", "link"],
    )
    section_one_body_right = RichTextField(
        features=["bold", "italic", "link"],
    )
    section_one_cta_text = models.CharField(max_length=255, null=True, blank=True)
    section_one_cta_link = models.ForeignKey(
        "wagtailcore.Page",
        related_name="+",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    section_two_text = models.TextField()
    section_two_cta_text = models.CharField(max_length=255, null=True, blank=True)
    section_two_cta_link = models.ForeignKey(
        "wagtailcore.Page",
        related_name="+",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    section_three_title = models.CharField(max_length=255)
    section_three_body = RichTextField(
        features=["bold", "italic", "link"],
    )
    section_three_image = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="+",
    )
    section_three_cta_text = models.CharField(max_length=255, null=True, blank=True)
    section_three_cta_link = models.ForeignKey(
        "wagtailcore.Page",
        related_name="+",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    section_four_title = models.CharField(max_length=255)
    section_four_body = RichTextField(
        features=["bold", "italic", "link"],
    )
    section_four_image = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="+",
    )
    section_four_cta_text = models.CharField(max_length=255, null=True, blank=True)
    section_four_cta_link = models.ForeignKey(
        "wagtailcore.Page",
        related_name="+",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    section_five_title = models.CharField(max_length=255)
    section_five_body = RichTextField(
        features=["bold", "italic", "link"],
    )
    section_five_image = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="+",
    )
    section_five_cta_text = models.CharField(max_length=255, null=True, blank=True)
    section_five_cta_link = models.ForeignKey(
        "wagtailcore.Page",
        related_name="+",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    section_six_title = models.CharField(max_length=255)
    section_six_body = RichTextField(
        features=["bold", "italic", "link"],
    )
    section_six_image = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="+",
    )
    section_six_cta_text = models.CharField(max_length=255, null=True, blank=True)
    section_six_cta_link = models.ForeignKey(
        "wagtailcore.Page",
        related_name="+",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    section_seven_text = models.CharField(max_length=255, null=True)

    content_panels = Page.content_panels + [
        FieldPanel("image"),
        FieldPanel("introduction"),
        MultiFieldPanel(
            [
                FieldPanel("section_one_body_left"),
                FieldPanel("section_one_body_right"),
                FieldRowPanel(
                    children=(
                        FieldPanel("section_one_cta_text"),
                        FieldPanel("section_one_cta_link"),
                    ),
                    heading="CTA",
                ),
            ],
            heading="Section One",
        ),
        MultiFieldPanel(
            [
                FieldPanel("section_two_text"),
                FieldRowPanel(
                    children=(
                        FieldPanel("section_two_cta_text"),
                        FieldPanel("section_two_cta_link"),
                    ),
                    heading="CTA",
                ),
            ],
            heading="Section Two",
        ),
        MultiFieldPanel(
            [
                FieldPanel("section_three_title"),
                FieldPanel("section_three_image"),
                FieldPanel("section_three_body"),
                FieldRowPanel(
                    children=(
                        FieldPanel("section_three_cta_text"),
                        FieldPanel("section_three_cta_link"),
                    ),
                    heading="CTA",
                ),
            ],
            heading="Section Three",
        ),
        MultiFieldPanel(
            [
                FieldPanel("section_four_title"),
                FieldPanel("section_four_image"),
                FieldPanel("section_four_body"),
                FieldRowPanel(
                    children=(
                        FieldPanel("section_four_cta_text"),
                        FieldPanel("section_four_cta_link"),
                    ),
                    heading="CTA",
                ),
            ],
            heading="Section Four",
        ),
        MultiFieldPanel(
            [
                FieldPanel("section_five_title"),
                FieldPanel("section_five_image"),
                FieldPanel("section_five_body"),
                FieldRowPanel(
                    children=(
                        FieldPanel("section_five_cta_text"),
                        FieldPanel("section_five_cta_link"),
                    ),
                    heading="CTA",
                ),
            ],
            heading="Section Five",
        ),
        MultiFieldPanel(
            [
                FieldPanel("section_six_title"),
                FieldPanel("section_six_image"),
                FieldPanel("section_six_body"),
                FieldRowPanel(
                    children=(
                        FieldPanel("section_six_cta_text"),
                        FieldPanel("section_six_cta_link"),
                    ),
                    heading="CTA",
                ),
            ],
            heading="Section Six",
        ),
        MultiFieldPanel([FieldPanel("section_seven_text")], heading="Section Seven"),
    ]
    template = "accomodation/page_two.html"

# retreat_accomodation_page
class PageThree(Page):
    image = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="+",
    )
    introduction_text = models.TextField(null=True, blank=True)
    section_one_title = models.CharField(max_length=256, null=True, blank=True)
    section_one_body = RichTextField(null=True, blank=True)
    section_one_cta_text = models.CharField(null=True, blank=True, max_length=255)
    section_one_cta_link = models.ForeignKey(
        "wagtailcore.Page",
        related_name="+",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    section_one_gallery = models.ForeignKey(
        Collection,
        limit_choices_to=~models.Q(name__in=["Root"]),
        null=True,
        related_name="+",
        blank=True,
        on_delete=models.SET_NULL,
        help_text="Select the image collection for this gallery.",
    )

    content_panels = Page.content_panels + [
        FieldPanel("image"),
        FieldPanel("introduction_text"),
        MultiFieldPanel(
            [
                FieldPanel("section_one_title"),
                FieldPanel("section_one_body"),
                FieldPanel("section_one_gallery"),
                FieldRowPanel(
                    children=(
                        FieldPanel("section_one_cta_text"),
                        FieldPanel("section_one_cta_link"),
                    ),
                    heading="CTA",
                ),
            ],
            heading="Secton One",
        ),
    ]

    template = "pages/page_three.html"
