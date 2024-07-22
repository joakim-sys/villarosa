from django import template
from wagtail.images.models import Image


register = template.Library()


@register.simple_tag
def get_images(gallery):
    images = Image.objects.filter(collection=gallery)
    return images
