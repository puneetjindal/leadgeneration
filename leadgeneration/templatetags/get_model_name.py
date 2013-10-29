from django import template

register=template.Library()


@register.filter(name='get_name')
def get_model_name(obj):
    model_base = str(obj.__class__).split('\'')
    return model_base[1]
