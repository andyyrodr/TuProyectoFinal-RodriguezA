from django import forms

from . import models


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = models.Categoria
        fields = "__all__"


class HistoriaForm(forms.ModelForm):
    class Meta:
        model = models.historia
        fields = "__all__"