from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="username")
    password = forms.CharField(widget=forms.PasswordInput(), label="password")
    remember = forms.BooleanField(label="exampleCheck1", required=False)

class FileForm(forms.Form):
    file=forms.FileField(label="file")

class AddForm(forms.Form):
   nit = forms.CharField(label="nit")
   nombre = forms.CharField(label="nombre")
   usuario = forms.CharField(label="usuario")
   clave = forms.CharField(label="clave") 
   direccion = forms.CharField(label="direccion") 
   correo = forms.CharField(label="correo") 