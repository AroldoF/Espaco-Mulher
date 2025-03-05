from django import forms
from apps.produtos.models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco', 'estoque', 'foto']
        labels = {
            'nome': 'Nome',
            'descricao': 'Descrição',
            'estoque': 'Estoque',
            'foto': 'Foto',
        }
        
        widgets = {
            "nome": forms.TextInput(attrs={'class': 'form-control'}),
            "descricao": forms.Textarea(attrs={'class': 'form-control'}),
            "preco": forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            "estoque": forms.NumberInput(attrs={'class': 'form-control'}),
            "foto": forms.FileInput(attrs={'class': 'form-control'}),
        }