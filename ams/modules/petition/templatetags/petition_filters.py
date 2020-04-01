from django import template

register = template.Library()

@register.filter(name='field_type')
def field_type(field, ftype):
    try:
        t = field.field.widget.__class__.__name__
        return t.lower() == ftype
    except:
        pass
    return False
