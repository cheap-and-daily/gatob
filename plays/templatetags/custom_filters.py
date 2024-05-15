from django import template

register = template.Library()


@register.filter
def duration_display(value):
    hours, minutes = divmod(value, 60)
    return f"{hours} ч. {minutes} м." if hours else f"{minutes} минут"
