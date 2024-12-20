from django.contrib import admin

# Register your models here.

from .models import Image, Annotation, AnnotationClass

admin.site.register(Image)
admin.site.register(Annotation)
admin.site.register(AnnotationClass)