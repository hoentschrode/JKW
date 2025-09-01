"""Snippet models."""

from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.fields import StreamField
from wagtail.models import Orderable
from wagtail.snippets.models import register_snippet
from modelcluster.models import ClusterableModel
from django.utils.translation import gettext_lazy as _
from wagtail.admin.panels import MultiFieldPanel, FieldPanel, InlinePanel
from wagtail.images import get_image_model_string

from home.blocks import HTML_BLOCKS


@register_snippet
class Carousel(ClusterableModel):
    """Model representing a carousel."""

    name = models.CharField(max_length=200, verbose_name=_("Name"))

    panels = [
        MultiFieldPanel(heading=_("Slider"), children=[FieldPanel("name")]),
        InlinePanel("carousel_slides", label=_("Slides")),  # type: ignore
    ]

    def __str__(self) -> str:
        return self.name  # type:ignore

    class Meta:
        verbose_name = _("Carousel")


class CarouselSlide(Orderable, models.Model):
    """Represents a single slide of a carousel."""

    carousel = ParentalKey(
        Carousel, related_name="carousel_slides", verbose_name=_("Carousel")
    )
    image = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name=_("Image"),
    )
    content = StreamField(HTML_BLOCKS, blank=True, use_json_field=True)
    panels = [FieldPanel("image")]

    class Meta(Orderable.Meta):
        verbose_name = _("Carousel slide")
