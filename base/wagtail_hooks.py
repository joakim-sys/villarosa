from wagtail import hooks
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet, SnippetViewSetGroup

from base.models import FooterHeader, NavigationMenu, NavigationMenuItem

class FooterHeaderViewSet(SnippetViewSet):
    model = FooterHeader
    # search_fields = ("text",)

class NavigationMenuViewSet(SnippetViewSet):
    model = NavigationMenu

class NavigationMenuItemViewSet(SnippetViewSet):
    model = NavigationMenuItem

class NavigationSnippetViewSetGroup(SnippetViewSetGroup):
    menu_label = 'Navigation Links'
    items = (NavigationMenuViewSet,)

class FooterSnippetViewSetGroup(SnippetViewSetGroup):
    menu_label = 'Footer Settings'
    items = (FooterHeaderViewSet,)


register_snippet(FooterSnippetViewSetGroup)
register_snippet(NavigationSnippetViewSetGroup)