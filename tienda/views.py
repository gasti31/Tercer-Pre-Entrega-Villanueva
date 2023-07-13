from django.shortcuts import render, redirect
from django.shortcuts import render
from .models import Producto
from .forms import BusquedaForm, FormularioProducto, FormularioBusqueda

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

def buscar_producto(request):
    if request.method == 'POST':
        formulario = FormularioBusqueda(request.POST)
        if formulario.is_valid():
            # Procesa los datos del formulario
            termino = formulario.cleaned_data['termino']
            # Realiza la búsqueda en la base de datos según el término
            productos = Producto.objects.filter(nombre__icontains=termino)
            # Renderiza los resultados en una plantilla o realiza las operaciones deseadas
            return render(request, 'resultados_busqueda.html', {'productos': productos})
    else:
        formulario = FormularioBusqueda()
    
    return render(request, 'buscar_producto.html', {'formulario': formulario})

def agregar_producto(request):
    if request.method == 'POST':
        formulario = FormularioProducto(request.POST)
        print(request.POST)
        
        if formulario.is_valid():
            nombre = formulario.cleaned_data['nombre']
            precio = formulario.cleaned_data['precio']
            categoria = formulario.cleaned_data['categoria']
            descripcion = formulario.cleaned_data['descripcion']

            producto = Producto(nombre=nombre, precio=precio, categoria=categoria, descripcion=descripcion)
            producto.save()
            return render(request, 'inicio.html')
    else:
        formulario = FormularioProducto()
    
    return render(request, 'agregar_producto.html', {'formulario': formulario})



