
from django import forms
from .models import Colaborador

class ColaboradorForm(forms.ModelForm):
    class Meta:
        model = Colaborador
        fields = ['nome_completo', 'cpf', 'funcao', 'status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nome_completo'].widget.attrs.update({'id': 'nome'})
        self.fields['cpf'].widget.attrs.update({'id': 'cpf'})
        self.fields['funcao'].widget.attrs.update({'id': 'funcao'})
        self.fields['status'].widget.attrs.update({'id': 'status'})