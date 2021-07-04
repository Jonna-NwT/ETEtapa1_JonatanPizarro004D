from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget

from .models import Colaborador



class RegisterColaborador(forms.ModelForm):
    class Meta:
        model = Colaborador
        fields = ['rutColaborador', 'imagen', 'nombreCompleto', 'telefono', 'direccion', 'email', 'pais', 'contraseña']                
        labels = {
            'rutColaborador' : 'Rut Colaborador:',
            'imagen' : 'Foto de identificacion:',
            'nombreCompleto' : 'Nombre Completo:',
            'telefono' : 'Telefono',
            'direccion' : 'Direccion:',
            'email' : 'Email:',
            'pais' : 'Pais:',
            'contraseña' : 'Contrasena'
        }
        widgets={
            'rutColaborador' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese Rut del Colaborador',
                    'maxlength' : '12',
                    'id' : 'rutColaborador',
                    'name' : 'rut_colaborador',
                    'required' : '',
                }
            ),
            'imagen' : forms.ClearableFileInput(
                attrs={
                    'class' : 'form-control', 
                    'accept' : 'image/*',
                    'id' : 'imagen',
                    'name' : 'imagen_',
                    'required' : ''
                }
            ),
            'nombreCompleto' : forms.TextInput(
                attrs={
                    'class' : 'form-control', 
                    'placeholder' : 'Ingrese su Nombre Completo',  
                    'maxlength' : '75',
                    'id' : 'nombreCompleto',
                    'name' : 'nombre_completo',
                    'required' : ''
                }
            ),  
            'telefono' : forms.NumberInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese un Numero Telefonico',
                    'id' : 'telefono',
                    'max' : '99999999999',
                    'min' : '0',
                    'name' : 'telefono_',
                    'required' : ''
                }
            ),
            'direccion' : forms.TextInput(
                attrs={
                    'class' : 'form-control', 
                    'placeholder' : 'Ingrese su Direccion',
                    'maxlength' : '35',
                    'id' : 'direccion',
                    'name' : 'direccion_',
                    'required' : ''
                }
            ),
            'email' : forms.EmailInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese su Email',
                    'id' : 'email',
                    'name' : 'email_',
                    'required' : ''
                }
            ),
            'pais' : forms.TextInput(
                attrs={
                    'class' : 'form-control', 
                    'maxlength' : '20',
                    'placeholder' : 'Ingrese su Pais',
                    'id' : 'pais',
                    'name' : 'pais_',
                    'required' : ''
                }
            ),
            'contraseña' : forms.TextInput(
                attrs={
                    'class' : 'form-control', 
                    'maxlength' : '15',
                    'placeholder' : 'Ingrese su Contrasena',
                    'id' : 'contrasena',
                    'name' : 'contraseña_',
                    'required' : ''
                }
            )
        }
        

class formModificarColaborador(forms.ModelForm):
    class Meta:
        model = Colaborador
        fields = ['rutColaborador', 'imagen', 'nombreCompleto', 'telefono', 'direccion', 'email', 'pais', 'contraseña']                
        labels = {
            'rutColaborador' : 'Rut Colaborador:',
            'imagen' : 'Foto de identificacion:',
            'nombreCompleto' : 'Nombre Completo:',
            'telefono' : 'Telefono',
            'direccion' : 'Direccion:',
            'email' : 'Email:',
            'pais' : 'Pais:',
            'contraseña' : 'Contrasena'
        }
        widgets={
            'rutColaborador' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese Rut del Colaborador',
                    'maxlength' : '12',
                    'id' : 'rutColaborador',
                    'readonly' : ''
                }
            ),
            'imagen' : forms.ClearableFileInput(
                attrs={
                    'class' : 'form-control', 
                    'accept' : 'image/*',
                    'id' : 'imagen'
                }
            ),
            'nombreCompleto' : forms.TextInput(
                attrs={
                    'class' : 'form-control', 
                    'placeholder' : 'Ingrese su Nombre Completo',  
                    'maxlength' : '75',
                    'id' : 'nombreCompleto'
                }
            ),  
            'telefono' : forms.NumberInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese un Numero Telefonico',
                    'id' : 'telefono',
                    'max' : '99999999999',
                    'min' : '0'
                }
            ),
            'direccion' : forms.TextInput(
                attrs={
                    'class' : 'form-control', 
                    'placeholder' : 'Ingrese su Direccion',
                    'maxlength' : '35',
                    'id' : 'direccion'
                }
            ),
            'email' : forms.EmailInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese su Email',
                    'maxlength' : '20',
                    'id' : 'email'
                }
            ),
            'pais' : forms.TextInput(
                attrs={
                    'class' : 'form-control', 
                    'maxlength' : '20',
                    'placeholder' : 'Ingrese su Pais',
                    'id' : 'pais'
                }
            ),
            'contraseña' : forms.TextInput(
                attrs={
                    'class' : 'form-control', 
                    'maxlength' : '15',
                    'placeholder' : 'Ingrese su Contrasena',
                    'id' : 'contrasena',
                    'readonly' : ''
                }
            )
        }