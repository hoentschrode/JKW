"""Content element blocks."""

from typing import Optional
from wagtail.blocks import (
    BooleanBlock,
    CharBlock,
    PageChooserBlock,
    StructBlock,
    StructValue,
)
from django.utils.translation import gettext_lazy as _
from wagtail.documents.blocks import DocumentChooserBlock


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
