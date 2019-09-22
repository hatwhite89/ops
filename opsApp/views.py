from django.shortcuts import render

# Create your views here.
from opsApp.models import Contenido,Medicamento


def main(request):

    return render(request,'index.html',)

def paginaContenido(request):
    id_contenido=request.GET['id_contenido']
    lista= Contenido.objects.filter(pk=id_contenido)
    lista_contenido=Contenido.objects.all()
    return render(request,'contenido.html',{'lista_contenido':lista,'listar_contenido':lista_contenido})

def listadoNacionalMedicamentos(request):
    listado_medicamentos= Medicamento.objects.all()
    return  render(request,'listado_nacional_medicamentos.html',{'listado_medicamentos':listado_medicamentos})

def publicacionGaceta(request):
    return render(request,'publicacion_gaceta.html')

def acuerdo(request):
    return render(request,'acuerdo.html')
