from django.db import models
from wagtail.models import Page


class BabySittingPage(Page):
    template = "services/babysitting_page.html"


class BikeHirePage(Page):
    template = "services/bike_hire_page.html"


class CarHireTransfersPage(Page):
    template = "services/car_hire_transfer.html"

class CelebrationCakesPage(Page):
    template = 'services/celebration_cakes.html'

class ChefHirePage(Page):
    template = 'services/chef_hire_page.html'

class RestaurantGuidePage(Page):
    template = "services/restaurant_guide.html"


class SupermarketsPage(Page):
    template = "services/supermarkets_page.html"


class ContactUsPage(Page):
    template = 'services/contact_page.html'