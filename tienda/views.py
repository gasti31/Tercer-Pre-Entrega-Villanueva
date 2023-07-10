from django.shortcuts import render
from django.shortcuts import render
from .models import Producto
from .forms import BusquedaForm

def inicio(request):
    productos = Producto.objects.all()
    form_busqueda = BusquedaForm()

    context = {'productos': productos, 'form_busqueda': form_busqueda}
    return render(request, 'inicio.html', context)

def buscar(request):
    form_busqueda = BusquedaForm(request.POST)

    if form_busqueda.is_valid():
        busqueda = form_busqueda.cleaned_data['busqueda']
        productos = Producto.objects.filter(nombre__icontains=busqueda)
    else:
        productos = Producto.objects.all()

    context = {'productos': productos, 'form_busqueda': form_busqueda}
    return render(request, 'inicio.html', context)


