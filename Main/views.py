import email
from re import T
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.
def inicio(self):

    plantilla = loader.get_template('inicio.html')
    documento = plantilla.render()

    return HttpResponse(documento)

def productoForm(request):
    if request.method == 'POST':
        miForm = ProductoForm(request.POST)

        print(miForm)

        if miForm.is_valid():
            info = miForm.cleaned_data

            producto = Producto(titulo = info['titulo'] , precio = info['precio'] , categoria = info['categoria'])

            producto.save()

            return render(request, "Main/inicio.html")

    else: 
        miForm = ProductoForm()

    return render(request, "Main/productoForm.html" , {"miForm":miForm})

def usuarioForm(request):
    if request.method == 'POST':
        miForm = UsuarioForm(request.POST)

        print(miForm)

        if miForm.is_valid():
            info = miForm.cleaned_data

            usuario = Usuario(username = info['username'] , email = info['email'])

            usuario.save()

            return render(request, "Main/inicio.html")

    else: 
        miForm = UsuarioForm()

    return render(request, "Main/usuarioForm.html" , {"miForm":miForm})

def compraForm(request):
    if request.method == 'POST':
        miForm = ComprasForm(request.POST)

        print(miForm)

        if miForm.is_valid():
            info = miForm.cleaned_data

            compras = Compras(titulo = info['titulo'] , precio = info['precio'] , fecha = info['fecha'])

            compras.save()

            return render(request, "Main/inicio.html")

    else: 
        miForm = ComprasForm()

    return render(request, "Main/compraForm.html" , {"miForm":miForm})


def busquedaProducto(request):


    return render(request, "Main/busquedaProducto.html")

def resultadoProducto(request):
    if request.GET["categoria"]:
        categoria = request.GET["categoria"]
        titulo = Producto.objects.filter(categoria__icontains = categoria)
        precio = Producto.objects.filter(categoria__icontains = categoria)

        return render(request, "Main/resultadoProducto.html" , {"categoria":categoria , "titulo": titulo , "precio":precio})

    else: 
        respuesta = "No enviaste datos"

        return HttpResponse(respuesta)

def busquedaUsuario(request):


    return render(request, "Main/busquedaUsuario.html")

def resultadoUsuario(request):
    if request.GET["username"]:
        username = request.GET["username"]
        email = Usuario.objects.filter(username__icontains = username)
       

        return render(request, "Main/resultadoUsuario.html" , {"email":email , "username": username})

    else: 
        respuesta = "No enviaste datos"

        return HttpResponse(respuesta)

def busquedaCompra(request):


    return render(request, "Main/busquedaCompra.html")

def resultadoCompra(request):
    if request.GET["titulo"]:
        titulo = request.GET["titulo"]
        fecha = Compras.objects.filter(titulo__icontains = titulo)
        precio = Compras.objects.filter(titulo__icontains = titulo)

        return render(request, "Main/resultadoCompra.html" , {"fecha":fecha , "titulo": titulo , "precio":precio})

    else: 
        respuesta = "No enviaste datos"

        return HttpResponse(respuesta)

def productos(request):
    datos_list = Producto.objects.all()
    diccionario = {'datos_list':datos_list}
    plantilla = loader.get_template('productos.html')
    documento = plantilla.render(diccionario)
    return HttpResponse(documento) 

def usuarios(request):
    datos_list = Usuario.objects.all()
    diccionario = {'datos_list':datos_list}
    plantilla = loader.get_template('usuario.html')
    documento = plantilla.render(diccionario)
    return HttpResponse(documento) 

def compras(request):
    datos_list = Compras.objects.all()
    diccionario = {'datos_list':datos_list}
    plantilla = loader.get_template('compras.html')
    documento = plantilla.render(diccionario)
    return HttpResponse(documento) 