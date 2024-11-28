from django import forms
from django.contrib.auth.models import User, Group
from .models import Usuario


class RegistroUsuarioForm(forms.ModelForm):
    username = forms.CharField(max_length=150, label="Nombre de usuario")
    telefono_personal = forms.CharField(max_length=20)
    tipo_de_usuario = forms.ModelChoiceField(
        queryset=Group.objects.all(), required=True
    )
    password = forms.CharField(
        widget=forms.PasswordInput, label="Contraseña", max_length=128
    )

    class Meta:
        model = Usuario
        fields = [
            "username",
            "rut",
            "nombres",
            "apellidos",
            "direccion",
            "telefono_personal",
            "correo_electronico",
            "tipo_de_usuario",
            "password",
            "enlace_whatsapp",
            "enlace_correo"
        ]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de usuario'}),
            'rut': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'RUT'}),
            'nombres': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombres'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellidos'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección'}),
            'telefono_personal': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono personal'}),
            'correo_electronico': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'}),
            'tipo_de_usuario': forms.Select(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}),
            'enlace_whatsapp': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enlace de WhatsApp'}),
            'enlace_correo': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enlace de correo electrónico'}),
        }

    def save(self, commit=True):
        usuario = super().save(commit=False)
        user = User.objects.create_user(
            username=self.cleaned_data["username"],
            email=self.cleaned_data["correo_electronico"],
            password=self.cleaned_data["password"],
        )
        usuario.user = user
        if commit:
            usuario.save()
            grupo = self.cleaned_data["tipo_de_usuario"]
            user.groups.add(grupo)
            user.save()
        return usuario
