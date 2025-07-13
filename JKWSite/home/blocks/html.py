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
