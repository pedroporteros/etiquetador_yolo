# Etiquetador de imágenes

## Instrucciones de ejecución

En primer lugar, creamos un entorno virtual de python. 

``` 
python3 -m venv etiquetador
```

y lo activamos:

```
.\etiquetador\Scripts\activate
```

Una vez activado el entorno virtual, procedemos a instalar las dependencias necesarias:

```
pip install -r requirements.txt
```

Una vez intsladas las dependencias, ya podemos lanzar el servidor:

```
python .\manage.py runserver
```

Este comando lanzará el servidor en http://127.0.0.1:8000/