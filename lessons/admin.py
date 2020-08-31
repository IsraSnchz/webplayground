from django.contrib import admin
from .models import Lesson
from embed_video.admin import AdminVideoMixin

# Register your models here.
class LessonAdmin(AdminVideoMixin, admin.ModelAdmin):
    list_display = ('title', 'video', 'order')
    
    class Media:
        css = {
            'all': ('lessons/css/custom_ckeditor.css',)
        }

admin.site.register(Lesson, LessonAdmin)