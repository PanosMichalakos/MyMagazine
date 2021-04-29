from django import template
from news.models import Post

register = template.Library()


@register.filter()
def filter_category(list, category):
    return list.filter(categories=category)


@register.filter()
def filter_featured(list, featured):
    return list.filter(featured=featured)


@register.filter()
def filter_slice(list, end):
    return list[:end]
