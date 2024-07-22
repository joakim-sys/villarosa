from wagtail.blocks import (
    CharBlock,
    StructBlock,
    StreamBlock,
    PageChooserBlock,
    RichTextBlock,
    RawHTMLBlock,
    TextBlock, ListBlock
)
from wagtail.images.blocks import ImageChooserBlock

class PostBlock(StructBlock):
    image = ImageChooserBlock()
    title = CharBlock()
    page = PageChooserBlock()
    subheading = TextBlock()

class PostStreamBlock(StreamBlock):
    post_block = PostBlock()

class Slide(StructBlock):
    # title = RichTextBlock(
    #     features=["h1", "h2", "h3", "h4", "h5", "h6", "bold", "italic", "br"]
    # )
    title = CharBlock()
    subheading = TextBlock()
    image = ImageChooserBlock()

    class Meta:
        icon = "image"
        label = "Slide"


class Carousel(StreamBlock):
    slide = Slide()


class AccomodationBody(StreamBlock):
    text = CharBlock(required=False)
    bullets = ListBlock(CharBlock())

class ImageStructBlock(StructBlock):
    image = ImageChooserBlock()

class ImageStream(StreamBlock):
    image_block = ImageStructBlock() 