from django import forms
from .models import Image, Annotation

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['name', 'image']
        
