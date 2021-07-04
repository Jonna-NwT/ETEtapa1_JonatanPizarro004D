from django.urls import path
from .views import index, crearColaborador,verTodos,modificarColaborador,eliminarColaborador

urlpatterns=[
    path('', index, name="index"),
    path('registrar_colaboradores', crearColaborador, name='crearColaborador'),
    path('ver-todos', verTodos, name='ver-todos'),
    path('modificar-colaborador/<id>', modificarColaborador, name='modificarColaborador'),
    path('eliminar-colaborador/<id>', eliminarColaborador, name='eliminarColaborador')
]