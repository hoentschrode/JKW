"""Content element blocks."""

from typing import Optional
from wagtail.blocks import (
    BooleanBlock,
    CharBlock,
    ChoiceBlock,
    PageChooserBlock,
    StreamBlock,
    StructBlock,
    StructValue,
)
from django.utils.translation import gettext_lazy as _
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.blocks import SnippetChooserBlock

from home.blocks.base import BaseStructBlock, BaseStructValue
from .html import HeadingBlock, RichTextBlock


class LinkStructValue(StructValue):
    """Generate title and link."""

    @property
    def get_title(self) -> Optional[str]:
        """Retrieve title."""
        title = self.get("title")
        if title:
            return title

        page = self.get("page_link")
        if page and page.live:
            return page.title

        document = self.get("document_link")
        if document:
            return document.title
        return self.get("external_link_url")

    @property
    def get_url(self) -> Optional[str]:
        """Retrieve URL."""
        page = self.get("page_link")
        external = self.get("external_link_url")
        if page and page.live and external:
            return f"{page.url}{external}"
        elif page and page.live:
            return page.url

        document = self.get("document_link")
        if document:
            return document.url

        return external


class LinkBlock(StructBlock):
    """A link to a page, document or external page."""

    page_link = PageChooserBlock(required=False, label=_("Page link"))
    title = CharBlock(
        required=False,
        max_length=255,
        label=_("Title"),
        help_text=_("Leave empty for document/page links to use their title."),
    )

    open_in_new_page_flag = BooleanBlock(required=False, label=_("Open in new page"))

    document_link = DocumentChooserBlock(required=False, label=_("Document link"))
    document_download_flag = BooleanBlock(required=False, label=_("Download document"))
    external_link_url = CharBlock(
        required=False, max_length=255, label=_("External URL")
    )

    class Meta:
        template = "home/blocks/link.html"
        label = _("Link")
        icon = "Link"
        value_class = LinkStructValue


class FlyerSwiperBlockValue(BaseStructValue):
    def get_js_initializer(self) -> str:
        return f"""
            _ = new Swiper('#{self.id}', {{
                speed:600, 
                loop:true,
                autoplay: {{ delay:5000, disableOnInteraction:false }},
                pagination: {{el:'#{self.id} > .swiper-pagination', type:'bullets',clickable:true}},
                slidesPerView:'auto'

            }});
        """.replace("\n", "")


class FlyerSwiperBlock(BaseStructBlock):
    """Shows all flyers as swiper."""

    class Meta:
        template = "home/blocks/flyer_swiper.html"
        icon = "resubmit"
        value_class = FlyerSwiperBlockValue


class BaseStreamBlock(StreamBlock):
    """Basic stream block."""

    heading = HeadingBlock()
    paragraph = RichTextBlock()


class CarouselBlockValue(BaseStructValue):
    def get_js_initializer(self) -> str:
        return f"""
            _ = new Swiper('#{self.id}', {{
                pagination:{{}}, 
                loop:true, 
                effect:'fade', 
                lazy:true,
                centeredSlides:true,
                autoplay: {{
                  delay:5000,
                  disableOnInteraction: false
                }}
            }});
        """.replace("\n", "")


class CarouselBlock(BaseStructBlock):
    """Carousel block to choose carousel snippet."""

    carousel = SnippetChooserBlock("home.Carousel")
    text = CharBlock(
        required=False,
        max_length=500,
        label=_("Overlay text"),
        help_text=_("Static overlay text for all slides"),
    )

    class Meta:
        icon = "image"
        label = _("Carousel")
        template = "home/blocks/carousel.html"
        value_class = CarouselBlockValue


class HeroBlock(BaseStructBlock):
    """Hero block."""

    background_image = ImageChooserBlock(
        required=False,
        label=_("Background image"),
        help_text=_("Hero background will be blurred by default"),
    )

    def __init__(self, local_blocks=None, search_index=True, **kwargs):
        local_blocks = [("content", StreamBlock(local_blocks))]
        super().__init__(local_blocks, search_index, **kwargs)

    class Meta:
        icon = "image"
        label = _("Hero")
        template = "home/blocks/hero.html"
