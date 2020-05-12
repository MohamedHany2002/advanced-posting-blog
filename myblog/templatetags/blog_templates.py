from django import template
from ..models import post
from django.db.models import Count

register=template.Library()

@register.simple_tag
def latest_posts():
    return post.published_posts.order_by('-publish')

@register.simple_tag
def most_commented_posts(num):
    return post.published_posts.annotate(count=Count('post_comments')).order_by('-count')[:num]

@register.filter
def upering(text):
    return text.upper()


# @register.inclusion_tag('base.html')
# def latest_posts():
#     return {'latest':post.objects.all()}