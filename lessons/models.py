from django.db import models
from ckeditor.fields import RichTextField
from embed_video.fields import EmbedVideoField

class Lesson(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200)
    video = EmbedVideoField(verbose_name="Video", max_length=200)
    content = RichTextField(verbose_name="Contenido")
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "leccion"
        verbose_name_plural = "lecciones"
        ordering = ['order', 'title']

    def __str__(self):
        return self.title


