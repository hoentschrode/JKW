"""Layout blocks."""

from wagtail import blocks
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.images.blocks import ImageChooserBlock
from django.utils.translation import gettext_lazy as _
import logging

from home.blocks.base import BaseStructBlock
from .content import LinkBlock
from .html import IconBlock

log = logging.getLogger(__name__)


class TileBlock(blocks.StructBlock):
    headline = blocks.CharBlock(required=False, max_length=200, label=_("Headline"))
    body = blocks.RichTextBlock(required=False, features=["bold", "italic"])
    link = LinkBlock(required=False, label=_("Link"))
    theme = blocks.ChoiceBlock(
        choices=[("default", _("Default theme")), ("green", _("Green theme"))],
        default="default",
        required=False,
        label=_("Tile theme"),
    )

    class Meta:
        template = "home/blocks/tile.html"
        group = _("Tiles")


class TileImageBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=False, label=_("Image"))

    class Meta:
        template = "home/blocks/tile_image.html"
        icon = "image"
        group = _("Tiles")


class CardBlock(blocks.StructBlock):
    icon = IconBlock()
    headline = blocks.CharBlock(required=False, max_length=200, label=_("Headline"))
    body = blocks.RichTextBlock(required=False, features=["bold", "italic"])

    class Meta:
        template = "home/blocks/card.html"
        group = _("Cards")


class CardImageBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=False, label=_("Image"))

    class Meta:
        template = "home/blocks/card_image.html"
        icon = "image"
        group = _("Cards")


class ColumnBlock(BaseStructBlock):
    """Block for a single column of grid/row block."""

    column_size = blocks.ChoiceBlock(
        choices=[
            ("", _("Automatic size")),
            ("12", _("Full row")),
            ("6", _("Half - 1/2 column")),
            ("4", _("Thirds - 1/3 column")),
            ("8", _("Thirds - 2/3 column")),
            ("3", _("Quarters - 1/4 column")),
            ("9", _("Quarters - 3/4 column")),
            ("2", _("Sixths - 1/6 column")),
            ("10", _("Sixths - 5/6 column")),
            ("1", _("Twelfths - 1/12 column")),
            ("5", _("Twelfths - 5/12 column")),
            ("7", _("Twelfths - 7/12 column")),
            ("11", _("Twelfths - 11/12 column")),
        ],
        default="",
        required=False,
        label=_("Column size"),
    )
    column_breakpoint = blocks.ChoiceBlock(
        choices=[
            ("", "Always expanded"),
            ("sm", "sm - Expand on small screens (phone, 576px) and larger"),
            ("md", "md - Expand on medium screens (tablet, 768px) and larger"),
            ("lg", "lg - Expand on large screens (laptop, 992px) and larger"),
            ("xl", "xl - Expand on extra large screens (wide monitor, 1200px)"),
        ],
        default="lg",
        required=False,
        label=_("Column breakpoint"),
    )

    theme = blocks.ChoiceBlock(
        choices=[
            ("transparent", _("Transparent (no colors)")),
            ("white", _("Black text on white")),
        ],
        default="transparent",
        required=True,
        label=_("Theme"),
    )

    round_borders = blocks.BooleanBlock(
        default=False, required=False, label=_("Rounded borders")
    )

    def __init__(self, local_blocks=None, search_index=True, **kwargs):
        stream_local_blocks = [
            (
                "content",
                blocks.StreamBlock(
                    [
                        ("row", RowBlock()),
                        ("tile", TileBlock()),
                        ("card", CardBlock()),
                    ]
                    + local_blocks
                    if local_blocks
                    else [],
                ),
            )
        ]
        super().__init__(stream_local_blocks, search_index, **kwargs)

    class Meta:
        label = _("Column block")
        template = "home/blocks/column.html"


class RowBlock(blocks.StructBlock):
    def __init__(self, local_blocks=None, search_index=True, **kwargs):
        local_blocks = [
            (
                "columns",
                blocks.StreamBlock(
                    [
                        ("tile", TileBlock()),
                        ("tile_image", TileImageBlock()),
                        ("card", CardBlock()),
                        ("card_image", CardImageBlock()),
                    ]
                ),
            ),
        ]
        super().__init__(local_blocks, search_index, **kwargs)

    class Meta:
        template = "home/blocks/row.html"
        icon = "table"


class GridBlock(BaseStructBlock):
    spacing = blocks.ChoiceBlock(
        choices=[("1", "1"), ("2", "2"), ("3", "3"), ("4", "4")],
        default="4",
        required=True,
        label=_("Spacing"),
        help_text=_("Gap between columns"),
    )

    def __init__(self, local_blocks=None, search_index=True, **kwargs):
        stream_local_blocks = [
            (
                "columns",
                blocks.StreamBlock(
                    [
                        ("column", ColumnBlock(local_blocks)),
                    ]
                ),
            )
        ]
        super().__init__(stream_local_blocks, search_index, **kwargs)

    # tile_image = TileImageBlock()
    # card_image = CardImageBlock()

    class Meta:
        template = "home/blocks/grid.html"


class FlyerSlideBlock(blocks.StructBlock):
    """A flyer swiper slide block."""

    image = ImageChooserBlock(required=True, label=_("Image"))
    flyer = DocumentChooserBlock(required=True, label=_("Flyer"))
    title = blocks.CharBlock(required=False, max_length=200, label=_("Title"))
    subtitle = blocks.CharBlock(required=False, max_length=200, label=_("Subtitle"))
    teaser_text = blocks.RichTextBlock(required=False, features=["bold", "italic"])

    class Meta:
        template = "home/blocks/flyer_slide.html"
