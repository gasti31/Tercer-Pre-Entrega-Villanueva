from django import forms

class FormularioProducto(forms.Form):
    nombre = forms.CharField(max_length=100)
    precio = forms.DecimalField(max_digits=8, decimal_places=2)
    descripcion = forms.CharField(widget=forms.Textarea)

class FormularioBusqueda(forms.Form):
    termino = forms.CharField(max_length=100)

class BusquedaForm(forms.Form):
    busqueda = forms.CharField(max_length=100)
    