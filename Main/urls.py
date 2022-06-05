from tkinter import N
from unicodedata import name
from django.urls import path 
from . import views

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('productoForm/' , views.productoForm , name="productoForm"),
    path('buscarProducto/' , views.busquedaProducto , name="buscarProducto"),
    path('resultadoProducto/' , views.resultadoProducto , name="resultadoProducto"),
    path('usuarioForm/', views.usuarioForm , name ="usuarioForm"),
    path('compraForm/', views.compraForm , name ="compraForm"),
    path('buscarUsuario/' , views.busquedaUsuario , name="buscarUsuario"),
    path('resultadoUsuario/' , views.resultadoUsuario , name="resultadoUsuario"),
    path('buscarCompra/' , views.busquedaCompra , name="buscarCompra"),
    path('resultadoCompra/' , views.resultadoCompra , name="resultadoCompra"),
    path('productos/' , views.productos, name="productos" ),
    path('compras/' , views.compras, name="compras" ),
    path('usuarios/' , views.usuarios , name="usuarios")



]