from django.db import models
from wagtail.models import Page


class HostRetreatPage(Page):
    template_name = "retreats/host_retreat_page.html"
    pass


class ReteatAccomodationPage(Page):
    template = "retreats/retreat_accomodation_page.html"


class CateringPage(Page):
    template = "retreats/retreat_catering_page.html"


class ExcursionsToursPage(Page):
    template = "retreats/excursions_tours_page.html"


class SoundBathHealingPage(Page):
    template = "retreats/sound_bath_healing_page.html"


class VoiceTherapyJuliaPage(Page):
    template = "retreats/voice_therapy_by_julia_page.html"


class YogaClassesPage(Page):
    template = "retreats/yoga_classes_page.html"


class TreatmentsPage(Page):
    template = "retreats/treatments_page.html"


