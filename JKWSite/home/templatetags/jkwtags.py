from django import template
import random
import string
from home.models.footer import Footer

register = template.Library()


@register.simple_tag()
def generate_random_id(prefix: str = "") -> str:
    """Returns a random id."""
    id = (
        "".join(random.choice(string.ascii_letters + string.digits) for _ in range(20))
        + "id"
    )
    return f"{prefix}{id}"


@register.inclusion_tag("home/includes/footer_text.html", takes_context=True)
def get_footer_text(context):
    footer_text = context.get("text", "")
    if not footer_text:
        instance = Footer.objects.filter(live=True).first()  # type: ignore
        footer_text = instance.text if instance else ""
    return {"text": footer_text}


@register.inclusion_tag("home/includes/footer_extra_slot.html", takes_context=True)
def get_footer_extra_slot(context):
    extra_slot = context.get("extra_slot", "")
    if not extra_slot:
        instance = Footer.objects.filter(live=True).first()  # type: ignore
        extra_slot = instance.extra_slot if instance else ""
    return {"extra_slot": extra_slot}
