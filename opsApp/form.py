from django import forms
from opsApp.models import sugerencias
class FormularioSugerencia(forms.Form):

    titulo =forms.CharField(required=True)
    correo=forms.EmailField()
    cuerpo=forms.CharField( widget=forms.Textarea)

    class Meta:
        model = sugerencias
        fields = ('titulo','correo','cuerpo')