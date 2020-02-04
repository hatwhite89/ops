from django.shortcuts import render, render_to_response,redirect
from django.http import HttpResponse
import json
# Create your views here.
from  opsApp.form  import FormularioSugerencia
from django.db.models import Q
from opsApp.models import Contenido,Medicamento,ArchivosGaceta,CategoriaMedicamento,link_android_descarga,link_ios_descarga, ayuda, sugerencias


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
    listado_medicamentos= Medicamento.objects.all().order_by('correlativo')
    return  render(request,'listado_nacional_medicamentos.html',{'listado_medicamentos':listado_medicamentos})

def archivo(request):
    lista_gaceta=ArchivosGaceta.objects.all()
    return render(request, 'archivos.html', {'lista_gaceta':lista_gaceta})

def acuerdo(request):
    return render(request,'acuerdo.html')

def listadoNacionalMedicamentos2(request):
    lista_categoria= CategoriaMedicamento.objects.all().order_by('correlativo')

    return render(request,'lnm2.html',{'lista_categoria':lista_categoria})
def listadoNacionalMedicamentosDetalle(request):
    id_categoria=request.GET['id_categoria']
    medicamento_list =Medicamento.objects.filter(categoria=id_categoria).order_by('correlativo')

    return render(request, 'lnm_detalle.html', {'listado_medicamentos': medicamento_list})

def politicas(request):

    return  render(request,'politicas.html')

def detalleBuscador(request):
    id_medicamento = request.GET['cod']
    medicamento_detalle = Medicamento.objects.filter(pk=id_medicamento)
    return render(request,'detalle_buscador.html',{'medicamento_list':medicamento_detalle})

def sugerencias_view(request):

    return render(request, 'sugerencia.html')

def respuesta_sugerencia(request):

    titulo_v = request.GET['titulo']
    correo = request.GET['correo']
    cuerpo = request.GET['cuerpo']

    newSugerencia = sugerencias(titulo =titulo_v,correo=correo ,cuerpo =cuerpo )

    newSugerencia.save()

    return redirect('/sugerencia')

def correoSugerencia(request):
    form = FormularioSugerencia(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            new_sugerencia = sugerencias(
                titulo= request.POST["titulo"],
                correo= request.POST["correo"],
                cuerpo= request.POST["cuerpo"]
            )
            new_sugerencia.save(form)

            return render(request,'index.html',{'bandera':"verdadero"})
    form = FormularioSugerencia()
    return render(request,'sugerencia.html',{'form':form})

def help(request):
    list_ayuda = ayuda.objects.all()
    return render(request,'ayuda.html',{'lista_medicamento':list_ayuda})

def search(request):
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(nombre_medicamento__icontains=query) |
            Q(codigo_atc__icontains=query)

        )
        results = Medicamento.objects.filter(qset).distinct()
    else:
        results = []
    return render_to_response("buscador.html", {
        "results": results,
        "query": query
    })
