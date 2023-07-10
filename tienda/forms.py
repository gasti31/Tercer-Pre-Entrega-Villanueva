from django import forms

class BusquedaForm(forms.Form):
    busqueda = forms.CharField(max_length=100)
    