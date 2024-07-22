from django.db import models
from django_extensions.db.fields import AutoSlugField
from wagtail.models import Page
from wagtail.contrib.settings.models import (
    register_setting,
    BaseSiteSetting,
    BaseGenericSetting,
)
from wagtail.admin.panels import (
    FieldPanel,
    PublishingPanel,
    MultiFieldPanel,
    InlinePanel,
)
from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey


@register_setting
class SiteSettings(BaseSiteSetting):
    title_suffix = models.CharField(
        verbose_name="Title Suffix", max_length=255, default="Villarosa"
    )

    panels = [FieldPanel("title_suffix")]


class FooterHeader(models.Model):
    text = models.CharField(max_length=256)

    panels = [
        FieldPanel("text"),
    ]

    def __str__(self):
        return self.text


class NavigationMenu(ClusterableModel):
    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from="title", editable=True)
    show_submenu = models.BooleanField(default=True)

    panels = [
        FieldPanel("title"),
        FieldPanel('show_submenu'),
        FieldPanel("slug"),
        InlinePanel("navigation_menu_items", label="Menu Item"),
    ]

    @property
    def first_child(self):
        return self.navigation_menu_items.first()

    def __str__(self):
        return self.title


class NavigationMenuItem(models.Model):
    link_title = models.CharField(max_length=100)
    link_url = models.CharField(max_length=500, blank=True, null=True)
    link_page = models.ForeignKey(Page, null=True, blank=True, on_delete=models.CASCADE)
    page = ParentalKey("NavigationMenu", related_name="navigation_menu_items",null=True)
    panels = [
        FieldPanel("link_title"),
        FieldPanel("link_url"),
        FieldPanel("link_page"),
    ]

    def __str__(self):
        return self.title

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        elif self.link_url:
            return self.link_url
        return '#'

    @property
    def title(self):
        if self.link_page and not self.link_title:
            return self.link_page.title
        elif self.link_title:
            return self.link_title
        return 'Missing Title'


@register_setting
class GenericSettings(ClusterableModel, BaseGenericSetting):
    x_url = models.URLField(verbose_name="X URL", blank=True)
    facebook_url = models.URLField(verbose_name="Facebook URL", blank=True)
    linkedin_url = models.URLField(verbose_name="LinkedIn URL", blank=True)
    instagram_url = models.URLField(verbose_name="Instagram URL", blank=True)
    youtube_url = models.URLField(verbose_name="YouTube URL", blank=True)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField()

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("address"),
                FieldPanel("phone"),
                FieldPanel("email"),
            ]
        ),
        MultiFieldPanel(
            [
                FieldPanel("linkedin_url"),
                FieldPanel("youtube_url"),
                FieldPanel("instagram"),
                FieldPanel("x_url"),
                FieldPanel("facebook_url"),
            ],
            "Social settings",
        ),
    ]


class ActivitiesPage(Page):
    template = "base/activities_page.html"


class BoatTripsTours(Page):
    template = "base/boat_trips_tours_page.html"


class PrivacyPolicyPage(Page):
    template = "base/privacy_policy_page.html"


class ReviewsPage(Page):
    template = "base/reviews.html"


class TermsConditionsPage(Page):
    template = "base/terms_conditions.html"
