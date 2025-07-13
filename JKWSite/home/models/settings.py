"""Settings module."""

from django.db import models
from wagtail.admin.panels import FieldPanel, FieldRowPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseGenericSetting, register_setting
from django.utils.translation import gettext_lazy as _
from wagtail.fields import RichTextField


@register_setting(icon="key")
class ContactSettings(BaseGenericSetting):
    """Contact settings."""

    name = models.CharField(
        null=True, blank=True, max_length=200, verbose_name=_("Name")
    )
    logo_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name=_("Logo"),
    )

    street = models.CharField(
        max_length=200, blank=True, null=True, verbose_name=_("Street")
    )
    zip_code = models.CharField(
        max_length=10, blank=True, null=True, verbose_name=_("Zip code")
    )
    city = models.CharField(
        max_length=200, blank=True, null=True, verbose_name=_("City")
    )

    phone_number = models.CharField(
        max_length=200, blank=True, null=True, verbose_name=_("Phone number")
    )
    email = models.EmailField(
        max_length=200, blank=True, null=True, verbose_name=_("Email")
    )

    panels = [
        FieldPanel("name"),
        FieldPanel("logo_image"),
        MultiFieldPanel(
            [
                FieldPanel("street"),
                FieldRowPanel([FieldPanel("zip_code"), FieldPanel("city")]),
            ],
            _("Address"),
        ),
        MultiFieldPanel(
            [FieldPanel("phone_number"), FieldPanel("email")], _("Contact")
        ),
    ]

    class Meta:
        verbose_name = _("Contact settings")


@register_setting(icon="time")
class OpeningHoursSettings(BaseGenericSetting):
    """Opening hours."""

    opening_hours = RichTextField(
        blank=True, features=["bold", "italic"], verbose_name=_("Opening hours")
    )

    panels = [FieldPanel("opening_hours")]

    class Meta:
        verbose_name = _("Opening hours")
