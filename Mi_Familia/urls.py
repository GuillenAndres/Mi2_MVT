from django.urls import path
from Mi_Familia.views import crear_familia, inicio

urlpatterns = [
    path('', inicio),
    path('familia/', crear_familia, name= 'Mi_FamiliaCrearFamilia'),
]