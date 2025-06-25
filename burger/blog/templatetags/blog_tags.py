from django import template
from django.db.models import Count

from blog.models import Post, Category

register = template.Library()

@register.simple_tag()
def get_all_categories():
    return Category.objects.all()



@register.simple_tag()
def recent_posts():
    return Post.objects.order_by('-created_at')[:4]