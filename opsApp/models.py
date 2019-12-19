from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Contenido(models.Model):
      titulo=models.CharField( max_length=200)
      cuerpo=RichTextField()
      fecha_publicacion=models.DateField()


      def __str__(self):
            return self.titulo
class NivelAtencion(models.Model):
      tipo_nivel=models.CharField(max_length=200)
      fecha_creacion= models.DateField()

      def __str__(self):
            return self.tipo_nivel


class SubCategoriaMedicamento(models.Model):
    nombre_categoria = models.CharField(max_length=200)
    fecha_creacion=models.DateField(null=True)

    def __str__(self):
          return self.nombre_categoria

class SegundaSubCategoriaMedicamento(models.Model):
      nombre_categoria = models.CharField(max_length=200)
      fecha_creacion=models.DateField(null=True)

      def __str__(self):
            return self.nombre_categoria

class CategoriaMedicamento(models.Model):
      nombre_categoria=models.CharField(max_length=200)
      fecha_creacion=models.DateField(null=True)
      correlativo=models.IntegerField(null=True)
      def __str__(self):
            return self.nombre_categoria

class FormaFarmaceutica(models.Model):
      nombre_forma=models.CharField(max_length=200,null=True)
      fecha_creacion=models.DateField(null=True)
      def __str__(self):
            return self.nombre_forma
class EnvasePrimario(models.Model):
      tipo_embase =models.CharField(max_length=200)
      fecha_creacion = models.DateField(null=True)
      def __str__(self):
            return self.tipo_embase

class ViasDeAdministracion(models.Model):
      nombre_via_administracion = models.CharField(max_length=200,null=True,blank=True)
      valor= models.CharField(null=True,blank=True,max_length=200)
      fecha_creacion = models.DateField(null=True)
      def __str__(self):

            return self.nombre_via_administracion+self.valor

class Medicamento(models.Model):
      correlativo = models.IntegerField(null= True)
      categoria = models.ForeignKey(CategoriaMedicamento)
      sub_categoria = models.ForeignKey(SubCategoriaMedicamento)
      segunda_subcategoria=models.ForeignKey(SegundaSubCategoriaMedicamento)
      codigo_atc = models.CharField(max_length=200)
      nombre_medicamento = models.CharField(max_length=200)
      contentracion = models.TextField(blank=True,null=True)
      forma_farmaceutica = models.ForeignKey(FormaFarmaceutica)
      via_de_administracion = models.ForeignKey(ViasDeAdministracion)
      envase_primario = models.ForeignKey(EnvasePrimario)
      nivel_de_atencion = models.ForeignKey(NivelAtencion)
      establecimiento = models.CharField(max_length=200,null=True,blank=True)
      lista_complementaria = models.CharField(max_length=200,null=True,blank=True)
      antibiotico_reserva = models.CharField(max_length=200,null=True,blank=True)
      restriccion_uso = models.CharField(max_length=200,null=True,blank=True)
      uaps=models.BooleanField(default=False)
      cis=models.BooleanField(default=False)
      p=models.BooleanField(default=False)
      hb=models.BooleanField(default=False)
      hg=models.BooleanField(default=False)
      hesp=models.BooleanField(default=False)
      inst=models.BooleanField(default=False)
      hpsiq=models.BooleanField(default=False)

      def __str__(self):
            return self.nombre_medicamento

class ArchivosGaceta(models.Model):
      nombre_del_archivo=models.CharField(max_length=200,null=True)
      descripcion= models.TextField(null=True)
      imagen_vista_previa= models.ImageField(upload_to="archivos/", null=True, blank=True)

      archivo = models.FileField(upload_to="archivos/", null=True, blank=True)
      def __str__(self):
            return self.nombre_del_archivo
class link_android_descarga(models.Model):
      nombre_link = models.CharField(max_length=200,null=True)
      link= models.TextField(null=True)
      def __str__(self):
            return self.nombre_link

class link_ios_descarga(models.Model):
      nombre_link = models.CharField(max_length=200,null=True)
      link= models.TextField(null=True)
      def __str__(self):
            return self.nombre_link

class sugerencias(models.Model):
      titulo= models.CharField(max_length=200,null=True)
      correo= models.CharField(max_length=200,null=True)
      cuerpo= models.TextField()
      estado= models.BooleanField(False)

      def __str__(self):
            if (self.estado == False):
                return self.titulo
