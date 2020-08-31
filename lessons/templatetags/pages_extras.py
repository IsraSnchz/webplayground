from django import template
from lessons.models import Lesson

register = template.Library()

@register.simple_tag
def get_lesson_list():
    lessons = Lesson.objects.all()
    return lessons