from wagtail import blocks
from django.utils.translation import gettext_lazy as _
import random
import string


class AdvancedSettingsBlock(blocks.StructBlock):
    """Separate block with advances settings for all base blocks."""

    custom_element_id = blocks.CharBlock(required=False, label=_("Custom element id"))

    class Meta:
        label = _("Advanced settings")
        icon = "cogs"
        collapsed = True


class BaseStructBlock(blocks.StructBlock):
    """Base block including the advanced settings panel."""

    advanced_settings_class = AdvancedSettingsBlock

    def __init__(self, local_blocks=None, search_index=True, **kwargs):
        if not local_blocks:
            local_blocks = ()

        local_blocks += (("settings", self.advanced_settings_class()),)
        super().__init__(local_blocks, search_index, **kwargs)


class BaseStructValue(blocks.StructValue):
    """Custom struct value to inject element id."""

    id = "?"

    def __init__(self, block, *args):
        super().__init__(block, *args)
        # Generate id and ensure, first char is a letter!
        self.id = "".join(
            random.choice(string.ascii_letters)
            + random.choice(string.ascii_letters + string.digits)
            for _ in range(19)
        )

    def get_id(self) -> str:
        return self.id
