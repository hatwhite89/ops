from django.shortcuts import render

# Create your views here.
from opsApp.models import Contenido,Medicamento,ArchivosGaceta,CategoriaMedicamento,link_android_descarga,link_ios_descarga


def main(request):
    link_android = link_android_descarga.objects.all()
    link_ios = link_android_descarga.objects.all()
    return render(request,'index.html',{'lista_android':link_android,'lista_ios':link_ios})

def paginaContenido(request):
    id_contenido=request.GET['id_contenido']
    lista= Contenido.objects.filter(pk=id_contenido)
    lista_contenido=Contenido.objects.all()
    return render(request,'contenido.html',{'lista_contenido':lista,'listar_contenido':lista_contenido})

def listadoNacionalMedicamentos(request):
    listado_medicamentos= Medicamento.objects.all()
    return  render(request,'listado_nacional_medicamentos.html',{'listado_medicamentos':listado_medicamentos})

def archivo(request):
    lista_gaceta=ArchivosGaceta.objects.all()
    return render(request, 'archivos.html', {'lista_gaceta':lista_gaceta})

def acuerdo(request):
    return render(request,'acuerdo.html')

def listadoNacionalMedicamentos2(request):
    lista_categoria= CategoriaMedicamento.objects.all()

    return render(request,'lnm2.html',{'lista_categoria':lista_categoria})
def listadoNacionalMedicamentosDetalle(request):
    id_categoria=request.GET['id_categoria']
    medicamento_list =Medicamento.objects.filter(categoria=id_categoria)

    return render(request, 'lnm_detalle.html', {'listado_medicamentos': medicamento_list})

def politicas(request):

    return  render(request,'politicas.html')