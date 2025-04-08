from django import template
from ..models import Subject
from django.db.models import Count

register = template.Library()

@register.simple_tag
def total_posts():
    return Subject.published.count()

@register.inclusion_tag('main_page/subject/latest_subjects.html')
def show_latest_subjects(count=3):
    latest_subjects = Subject.published.order_by('-publish')[:count]
    return {'latest_subjects': latest_subjects}

@register.simple_tag
def get_most_liked_subjects(count=3):
    return Subject.published.annotate(total_likes=Count('like')).order_by('-total_likes')[:count]