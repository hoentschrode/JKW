from django.db.models import PROTECT, CharField, ForeignKey, TextField
from wagtail.fields import RichTextField, StreamField
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
    parent_page_types = ["wagtailcore.Page"]
    # Fields
    body = StreamField(LAYOUT_BLOCKS, null=True, blank=True)
    # Panels
    content_panels = Page.content_panels + [FieldPanel("body")]

    class Meta:
        verbose_name = _("Home page")


class MaintenancePage(Page):
    """A special page shown in maintenance phases."""

    template = "home/pages/maintenance.html"
    parent_page_types = ["wagtailcore.Page"]
    subpage_types = []
    # Fields
    headline = CharField(
        blank=True, verbose_name=_("Headline"), help_text=_("Headline text")
    )
    sub_headline = CharField(
        blank=True, verbose_name=_("Sub headline"), help_text=_("Subtitle")
    )
    message = RichTextField(
        blank=True,
        verbose_name=_("Message text"),
        help_text=_("Short message to the user"),
    )
    # Panels
    content_panels = Page.content_panels + [
        FieldPanel("headline"),
        FieldPanel("sub_headline"),
        FieldPanel("message"),
    ]

    class Meta:
        verbose_name = _("Maintenance page")


class FlyerPage(Page):
    """A page for a downloadable flyer."""

    subtitle = CharField(
        blank=True, verbose_name=_("Subtitle"), help_text=_("Additional sub title")
    )
    image = ForeignKey(
        "wagtailimages.Image",
        null=False,
        blank=False,
        on_delete=PROTECT,
        related_name="+",
        help_text=_("Descriptive sample image (cropped to be rectangled)."),
    )
    document = ForeignKey(
        get_document_model(),
        null=False,
        blank=False,
        on_delete=PROTECT,
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
        FieldPanel("description"),
    ]

    parent_page_types = ["FlyerIndexPage"]
    subpage_types = []
    template = "home/pages/flyer.html"

    class Meta:
        verbose_name = _("Flyer page")


class FlyerIndexPage(Page):
    """Index page showing all flyers."""

    introduction = TextField(
        verbose_name=_("Introduction"),
        help_text=_("Text to describe the page"),
        blank=True,
    )

    content_panels = Page.content_panels + [FieldPanel("introduction")]
    subpage_types = ["FlyerPage"]
    parent_page_types = ["HomePage"]
    template = "home/pages/flyer_index.html"

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["flyers"] = (
            FlyerPage.objects.descendant_of(self).live().order_by("path")
        )
        return context

    class Meta:
        verbose_name = _("Flyer index page")


class StandardPage(Page):
    """Simple page just using header, breadcrumb and footer."""

    body = StreamField(CONTENT_BLOCKS, verbose_name=_("Page body"), blank=True)

    content_panels = Page.content_panels + [FieldPanel("body")]
    template = "home/pages/page.html"
    parent_page_types = ["HomePage", "StandardPage", "FlyerIndexPage"]
