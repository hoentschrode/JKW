"""Basic html blocks."""

from wagtail import blocks
from django.utils.translation import gettext_lazy as _


class RichTextBlock(blocks.RichTextBlock):
    pass


class IconBlock(blocks.StructBlock):
    icon_name = blocks.CharBlock(
        required=False, label=_("Bootstrap-icon name"), max_length=100
    )

    class Meta:
        template = "home/blocks/icon.html"
        label = "Icon"
        icon = "image"
        help_text = _(
            'Insert a boostrap icon name here. Look up: <a href="https://icons.getbootstrap.com/" target="_blank">here</a>'
        )


class HeadingBlock(blocks.StructBlock):
    """Custom heading block for H1...H4 elements."""

    text = blocks.CharBlock(required=True, label=_("Heading text"))
    level = blocks.ChoiceBlock(
        choices=[
            ("", _("Select header level")),
            ("h1", "H1"),
            ("h2", "H2"),
            ("h3", "H3"),
            ("h4", "H4"),
        ],
        blank=True,
        required=True,
        default="h1",
    )

    class Meta:
        icon = "title"
        template = "home/blocks/heading.html"
        description = _("A heading on level 1..4")
