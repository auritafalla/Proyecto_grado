from django import forms
from .models import Usuario, Solicitante, evento

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombres', 'apellidos', 'tipo_documento', 'numero_documento', 'correo_sena', 'area_bienestar', 'contrasena', 'celular']

        widgets = {
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_documento': forms.TextInput(attrs={'class': 'form-control'}),
            'numero_documento': forms.NumberInput(attrs={'class': 'form-control'}),
            'celular': forms.TextInput(attrs={'class': 'form-control'}),
            'correo_sena': forms.EmailInput(attrs={'class': 'form-control'}),
            'area_bienestar': forms.TextInput(attrs={'class': 'form-control'}),
        }
 