from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from .forms import ImageForm
from .models import *
import json
import random

# Create your views here.

# Vista para manejar la carga de imágenes
def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('etiquetador_app:upload_image')
    else:
        form = ImageForm()
    return render(request, 'etiquetador_app/upload_image.html', {'form': form})

# Vista para listar las imágenes
def image_list(request):
    images = Image.objects.all()
    return render(request, 'etiquetador_app/list_image.html', {'images': images})

# Vista para eliminar una imagen
def delete_image(request, image_id):
    image = get_object_or_404(Image, pk=image_id)
    image.delete()
    return redirect('etiquetador_app:image_list')

# Vista para etiquetar una imagen
def label_image(request, image_id):
    image = get_object_or_404(Image, pk=image_id)
    annotations = image.annotations.all()
    return render(request, 'etiquetador_app/label_image.html', {'image': image, 'annotations': annotations})

# Vista para guardar las anotaciones
def save_annotations(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        image = get_object_or_404(Image, id=data['image_id'])
        
        if not data['annotations']:
            return JsonResponse({'status': 'error', 'message': 'No se han realizado anotaciones'}, status=400)

        image.annotations.all().delete()

        for annotation in data['annotations']:
            Annotation.objects.create(
                image=image,
                x_center=annotation['x'] + annotation['width'] / 2,
                y_center=annotation['y'] + annotation['height'] / 2,
                width=annotation['width'],
                height=annotation['height'],
                category=annotation['class']
            )
        return JsonResponse({'status': 'success'})

# Vista para cargar las anotaciones
def load_annotations(request, image_id):
    annotations = Annotation.objects.filter(image_id=image_id)
    data = [
        {
            "class": annotation.category,
            "x": annotation.x_center - annotation.width / 2,
            "y": annotation.y_center - annotation.height / 2,
            "width": annotation.width,
            "height": annotation.height,
        }
        for annotation in annotations
    ]
    return JsonResponse({"annotations": data})

# Vista para descargar las anotaciones en formato YOLO
def download_yolo(request, image_id):
    image = get_object_or_404(Image, id=image_id)
    annotations = image.annotations.all()

    yolo_data = "\n".join([
        f"0 {ann.x_center} {ann.y_center} {ann.width} {ann.height}"
        for ann in annotations
    ])

    response = HttpResponse(yolo_data, content_type='text/plain')
    response['Content-Disposition'] = f'attachment; filename="{image.name}.txt"'
    return response

# Función para generar un color aleatorio
def random_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

# Vista para manejar las clases
def manage_classes(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        class_name = data.get('name')

        # Comprueba si la clase ya existe
        annotation_class, created = AnnotationClass.objects.get_or_create(
            name=class_name,
            defaults={'color': random_color()}
        )

        if created:
            return JsonResponse({'status': 'success', 'class': {'name': annotation_class.name, 'color': annotation_class.color}})
        else:
            return JsonResponse({'status': 'error', 'message': 'La clase ya existe'}, status=400)
    else:
        # Devuelve la lista de clases
        classes = list(AnnotationClass.objects.values('name', 'color'))
        return JsonResponse({'classes': classes})
    

