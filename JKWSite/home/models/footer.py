"""Footer snippet."""

from django.db import models
from wagtail.admin.panels import FieldPanel, PublishingPanel
from wagtail.fields import RichTextField, StreamField
from wagtail.models import (
    DraftStateMixin,
    PreviewableMixin,
    RevisionMixin,
)
from wagtail.snippets.models import register_snippet
from django.utils.translation import gettext_lazy as _
from django.utils.translation import gettext
from home.blocks import CONTENT_BLOCKS


@register_snippet
class Footer(DraftStateMixin, RevisionMixin, PreviewableMixin, models.Model):
    text = RichTextField(
        blank=True,
        features=["bold", "italic", "link"],
        verbose_name=_("Text"),
    )
    extra_slot = StreamField(
        CONTENT_BLOCKS, null=True, blank=True, verbose_name=_("Extra footer slot")
    )

    panels = [FieldPanel("text"), FieldPanel("extra_slot"), PublishingPanel()]

    def __str__(self):
        return gettext("Footer text")

    class Meta:
        verbose_name = _("Footer text")
        verbose_name_plural = _("Footer texts")
