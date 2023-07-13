from django import forms

class FormularioProducto(forms.Form):
    nombre = forms.CharField()
    precio = forms.DecimalField()
    descripcion = forms.CharField()
    categoria = forms.CharField()
    

class FormularioBusqueda(forms.Form):
    termino = forms.CharField(max_length=100)

class BusquedaForm(forms.Form):
    busqueda = forms.CharField(max_length=100)
    