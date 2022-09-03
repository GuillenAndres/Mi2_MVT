from django.shortcuts import render
from .models import Familia


def inicio(request):
    return render(request, 'index.html')



def familia(request):
    return render(request, 'Mi_Familia/familia.html', context={})

def crear_familia(request):
    hogar = Familia.objects.create(
        pdr_nombre = 'Roberto', 
        pdr_edad = 36 , 
        pdr_nacimiento = '1986-05-05',
        
        mdr_nombre = 'Marta', 
        mdr_edad = 31 , 
        mdr_nacimiento = '1990-06-01',

        hjs_nombre = 'Juan', 
        hjs_edad = 10 , 
        hjs_nacimiento = '2012-05-01',
        
        )
    context = {'hogar':hogar}
    return render(request, 'Mi_Familia/familia.html', context)