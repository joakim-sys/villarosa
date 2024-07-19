from wagtail.blocks import (
    CharBlock,
    StructBlock,
    StreamBlock,
    PageChooserBlock,
    RichTextBlock,
    RawHTMLBlock,
    TextBlock
)
from wagtail.images.blocks import ImageChooserBlock


class Slide(StructBlock):
    # title = RichTextBlock(
    #     features=["h1", "h2", "h3", "h4", "h5", "h6", "bold", "italic", "br"]
    # )
    title = RawHTMLBlock()
    subheading = TextBlock()
    image = ImageChooserBlock()

    class Meta:
        icon = "image"
        label = "Slide"


class Carousel(StreamBlock):
    slide = Slide()
