from django.contrib import admin

# Register your models here.
from opsApp.models import Contenido,Medicamento,CategoriaMedicamento,SubCategoriaMedicamento,ViasDeAdministracion,EnvasePrimario,FormaFarmaceutica,SegundaSubCategoriaMedicamento,NivelAtencion,ArchivosGaceta,link_android_descarga,link_ios_descarga,sugerencias,ayuda
admin.site.register(EnvasePrimario)
admin.site.register(NivelAtencion)
admin.site.register(FormaFarmaceutica)
admin.site.register(ViasDeAdministracion)
admin.site.register(Contenido)
admin.site.register(Medicamento)
admin.site.register(CategoriaMedicamento)
admin.site.register(SubCategoriaMedicamento)
admin.site.register(SegundaSubCategoriaMedicamento)
admin.site.register(ArchivosGaceta)
admin.site.register(link_android_descarga)
admin.site.register(link_ios_descarga)
admin.site.register(sugerencias)

admin.site.register(ayuda)

