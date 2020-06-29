from django import template
from portsite.models import Quote
import random

register = template.Library()

@register.simple_tag
def length(text, extra):
	return (len(text) / 1.5) + 220 + extra

@register.simple_tag
def randomQuote():
	quotes = Quote.objects.all()
	print((random.choice(quotes)).quote)
	return random.choice(quotes)
