"""Layout blocks."""

from wagtail import blocks
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.images.blocks import ImageChooserBlock
from django.utils.translation import gettext_lazy as _
import logging
from .content import LinkBlock
from .html import IconBlock
from typing import List
import random
import string

log = logging.getLogger(__name__)


class ColumnMixin(blocks.StructBlock):
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


class TileBlock(ColumnMixin, blocks.StructBlock):
    headline = blocks.CharBlock(required=False, max_length=200, label=_("Headline"))
    body = blocks.RichTextBlock(required=False, features=["bold", "italic"])
    link = LinkBlock(required=False, label=_("Link"))

    class Meta:
        template = "home/blocks/tile.html"
        group = _("Tiles")


class TileImageBlock(ColumnMixin, blocks.StructBlock):
    image = ImageChooserBlock(required=False, label=_("Image"))

    class Meta:
        template = "home/blocks/tile_image.html"
        icon = "image"
        group = _("Tiles")


class CardBlock(ColumnMixin, blocks.StructBlock):
    icon = IconBlock()
    headline = blocks.CharBlock(required=False, max_length=200, label=_("Headline"))
    body = blocks.RichTextBlock(required=False, features=["bold", "italic"])

    class Meta:
        template = "home/blocks/card.html"
        group = _("Cards")


class CardImageBlock(ColumnMixin, blocks.StructBlock):
    image = ImageChooserBlock(required=False, label=_("Image"))

    class Meta:
        template = "home/blocks/card_image.html"
        icon = "image"
        group = _("Cards")


class RowBlock(ColumnMixin, blocks.StructBlock):
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


class GridBlock(blocks.StreamBlock):
    row = RowBlock()
    tile = TileBlock()
    tile_image = TileImageBlock()
    card = CardBlock()
    card_image = CardImageBlock()

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


class SwiperBlock(blocks.StreamBlock):
    flyer_slide_block = FlyerSlideBlock()

    def __init__(self, local_blocks=None, search_index=True, **kwargs):
        self._id = None
        super().__init__(local_blocks, search_index, **kwargs)

    @property
    def id(self) -> str:
        if self._id is None:
            self._id = (
                "".join(
                    random.choice(string.ascii_letters + string.digits)
                    for _ in range(20)
                )
                + "id"
            )
        return self._id

    @property
    def extra_js_static_libs(self) -> List[str]:
        return ["js/swiper-bundle.min.js"]

    @property
    def inline_js(self) -> List[str]:
        return [
            f"""
            const swiper_{self.id} = new Swiper('#swiper_{self.id}', {{
              speed: 600,
              loop: true,
              //autoplay: {{
              //  delay: 5000,
              //  disableOnInteraction: false
             // }},
              pagination: {{
                el: '#{self.id}_pagination',
                type: 'bullets',
                clicbable: true
              }},
              slidesPerView: 1,
              breakpoints:{{
                768: {{slidesPerView:3}},
                1200: {{slidesPerView:4}}
              }}
            }});
        """
        ]

    def render(self, value, context=None):
        return super().render(value, context)

    class Meta:
        template = "home/blocks/swiper.html"
