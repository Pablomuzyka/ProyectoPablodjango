from django.http import HttpResponse
from django.shortcuts import render

from .models import familiar

# Create your views here.


def inicioApp (request):
    return render(request,'AppFamilia/inicio.html')

def Familia(request):
    familiar_1=familiar(nombre='gustavo',apellido='ruster',edad='45',dni='12457896')    
    familiar_2=familiar(nombre='fabiana',apellido='guzman',edad='38',dni='23568947')    
    familiar_3=familiar(nombre='franco',apellido='oslo',edad='15',dni='40758796') 
    familiar_1.save()
    familiar_2.save()
    familiar_3.save()
    texto_1=f"este es mi tio {familiar_1.nombre} {familiar_1.apellido} tiene {familiar_1.edad} ,  esta es mi tia {familiar_2.nombre} {familiar_2.apellido} tiene {familiar_2.edad} , este es mi primo {familiar_3.nombre} {familiar_3.apellido} tiene {familiar_3.edad}"
    return HttpResponse(texto_1)   
 