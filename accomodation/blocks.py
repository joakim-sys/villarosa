from wagtail.blocks import CharBlock, StreamBlock, StructBlock, RichTextBlock


class FeatureBlock(StructBlock):
    # heading = CharBlock(help_text="Title of the accommodation feature")
    description = RichTextBlock(
        features=["bold", "italic", "link"],
        help_text="Description of the first accommodation feature",
    )


class DescriptionBlock(StreamBlock):
    feature = FeatureBlock()
