from django import template

register = template.Library()

@register.simple_tag
def length(text, extra):
	return (len(text) / 1.5) + 220 + extra
