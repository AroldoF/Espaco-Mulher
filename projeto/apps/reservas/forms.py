from django import forms
from apps.reservas.models import ReservaProduto, ReservaServico


class ReservaProdutoForms(forms.ModelForm):
    class Meta:
        model = ReservaProduto
        fields = ["produto", "quantidade_comprada", "data_reservada"]
        labels = {
            "produto": "Produto",
            "quantidade_comprada": "Quantidade que deseja comprar",
            "data_reservada": "Data reservada",
        }
        widgets = {
            "produto": forms.Select(attrs={"class": "form-control"}),
            "quantidade_comprada": forms.NumberInput(attrs={"class": "form-control"}),
            "data_reservada": forms.DateTimeInput(
                attrs={"class": "form-control", "type": "datetime-local"}
            ),  # Aqui!
        }


class ReservaServicoForms(forms.ModelForm):
    class Meta:
        model = ReservaServico
        fields = ["servico", "data_reservada"]
        labels = {
            "servico": "Serviço",
            "data_reservada": "Data reservada",
        }
        widgets = {
            "servico": forms.Select(attrs={"class": "form-control"}),
            "data_reservada": forms.DateTimeInput(
                attrs={"class": "form-control", "type": "datetime-local"}
            ),  # Aqui também!
        }
