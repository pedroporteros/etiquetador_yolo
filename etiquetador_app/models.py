from django.db import models

# Create your models here.

class Image(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.name
    
class Annotation(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='annotations')
    category = models.CharField(max_length=50)
    x_center = models.FloatField()
    y_center = models.FloatField()
    width = models.FloatField()
    height = models.FloatField()

class AnnotationClass(models.Model):
    name = models.CharField(max_length=50, unique=True)
    color = models.CharField(max_length=7)

    def __str__(self):
        return self.name