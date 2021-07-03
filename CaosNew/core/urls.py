from django.urls import path
from .views import index, crearColaborador

urlpatterns=[
    path('', index, name="index"),
    path('registrar_colaboradores', crearColaborador, name='crearColaborador'),
]