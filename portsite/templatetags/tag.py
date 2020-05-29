from django import template

register = template.Library()

@register.simple_tag
def length(text):
	print((len(text) / 1.5) + 220)
	return (len(text) / 1.5) + 220
