from django import forms

class ProductoForm(forms.Form):
    titulo = forms.CharField(max_length=40)
    categoria = forms.CharField(max_length=30)
    precio = forms.IntegerField()

class UsuarioForm(forms.Form):
    username = forms.CharField(max_length=30)
    email = forms.EmailField()

class ComprasForm(forms.Form):
    precio = forms.IntegerField()
    titulo = forms.CharField(max_length=40)
    fecha = forms.DateField()