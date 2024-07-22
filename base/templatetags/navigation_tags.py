from django import template
from wagtail.models import Page

from base.models import FooterHeader, NavigationMenu

register = template.Library()


@register.inclusion_tag("base/include/footer_header.html", takes_context=True)
def get_footer_header(context):
    footer_header = context.get("footer_header", "")
    if not footer_header:
        instance = FooterHeader.objects.first()
        footer_header = instance.text if instance else ""
    return {
        "footer_header": footer_header,
    }

@register.simple_tag
def get_footer_links():
    return Page.objects.live().exclude(depth=1)


@register.simple_tag()
def get_menu():
    return NavigationMenu.objects.all()