from django.urls import path
from etiquetador_app.views import *

app_name = 'etiquetador_app'

urlpatterns = [
    path('', upload_image, name='upload_image'),
    path('list_images/', image_list, name='image_list'),
    path('delete_image/<int:image_id>/', delete_image, name='delete_image'),
    path('label/<int:image_id>/', label_image, name='label_image'),
    path('save_annotations/', save_annotations, name='save_annotations'),
    path('download_yolo/<int:image_id>/', download_yolo, name='download_yolo'),
    path('manage_classes/', manage_classes, name='manage_classes'),
    path('load_annotations/<int:image_id>/', load_annotations, name='load_annotations'),
]