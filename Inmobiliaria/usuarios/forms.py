from django import forms
from django.contrib.auth.models import User, Group
from .models import Usuario


class RegistroUsuarioForm(forms.ModelForm):
    telefono_personal = forms.CharField(max_length=20)
    tipo_de_usuario = forms.ModelChoiceField(
        queryset=Group.objects.all(), required=True
    )

    class Meta:
        model = Usuario
        fields = [
            "rut",
            "nombres",
            "apellidos",
            "direccion",
            "telefono_personal",
            "correo_electronico",
            "tipo_de_usuario",
        ]

    def save(self, commit=True):
        usuario = super().save(commit=False)
        user = User.objects.create_user(
            username=self.cleaned_data["rut"],
            email=self.cleaned_data["correo_electronico"],
            password=None,
        )
        usuario.user = user
        if commit:
            usuario.save()
            grupo = self.cleaned_data["tipo_de_usuario"]
            user.groups.add(grupo)
            user.save()
        return usuario
