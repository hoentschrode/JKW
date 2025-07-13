from django.db.models import SET_NULL, CharField, ForeignKey, TextField
from wagtail.fields import StreamField
from wagtail.models import Page
from django.utils.translation import gettext_lazy as _
from wagtail.admin.panels import FieldPanel, FieldRowPanel
from home.blocks import CONTENT_BLOCKS, LAYOUT_BLOCKS
from wagtail.documents import get_document_model


class HomePage(Page):
    """
    _The_ home page.
    Usually a page without breadcrumb navigation bar.
    """

    template = "home/pages/home.html"
    max_count = 1
    # Fields
    body = StreamField(LAYOUT_BLOCKS, null=True, blank=True)
    # Panels
    content_panels = Page.content_panels + [FieldPanel("body")]

    class Meta:
        verbose_name = _("Home page")


class SimplePage(Page):
    template = "home/pages/page.html"
    # Fields
    body = StreamField(CONTENT_BLOCKS, null=True, blank=True)
    content_panels = Page.content_panels + [FieldPanel("body")]

    class Meta:
        verbose_name = _("Page")


class FlyerPage(Page):
    subtitle = CharField(
        blank=True, verbose_name=_("Subtitle"), help_text=_("Additional sub title")
    )
    image = ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=SET_NULL,
        related_name="+",
        help_text=_("Descriptive sample image (cropped to be rectangled)."),
    )
    document = ForeignKey(
        get_document_model(),
        null=True,
        blank=True,
        on_delete=SET_NULL,
        related_name="+",
    )
    description = TextField(
        blank=True, verbose_name=_("Description"), help_text=_("Short description text")
    )

    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
        FieldRowPanel(
            [
                FieldPanel("image"),
                FieldPanel("document"),
            ]
        ),
    ]

    parent_page_types = ["FlyerIndexPage"]
    subpage_types = []


class FlyerIndexPage(Page):
    introduction = TextField(
        verbose_name=_("Introduction"),
        help_text=_("Text to describe the page"),
        blank=True,
    )

    content_panels = Page.content_panels + [FieldPanel("introduction")]
    subpage_types = ["FlyerPage"]
