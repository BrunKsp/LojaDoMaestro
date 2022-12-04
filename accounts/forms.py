from django import forms 
from .models import Perfil


class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ('nome_completo','cpf', 'cep' , 'email' ,'telefone','estado','cidade')