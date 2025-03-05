from django import forms
from apps.servicos.models import Servico

class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        #'produto','valor_total'
        fields = ['nome', 'descricao', 'preco', 'tempo_duracao', 'foto']
        labels = {
            'nome': 'Nome',
            'descricao': 'Descrição',
            'tempo_duracao': 'Tempo de duração',
            'foto': 'Foto',
        }
        
        widgets = {
            "nome": forms.TextInput(attrs={'class': 'form-control'}),
            "descricao": forms.Textarea(attrs={'class': 'form-control'}),
            "preco": forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            "tempo_duracao": forms.NumberInput(attrs={'class': 'form-control'}),
            "foto": forms.FileInput(attrs={'class': 'form-control'}),
        }