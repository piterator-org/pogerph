from math import ceil

from django import template

from blog.models import Category

register = template.Library()


@register.simple_tag
def get_categories(split=False):
    categories = Category.objects.all()
    if split:
        length = ceil(len(categories) / 2)
        return categories[:length], categories[length:]
    return categories
