from django import forms
from package.models import paquete

class PackageForms(forms.ModelForm):
    class Meta:
        model = paquete
        fields = ['nombre', 'precio', 'comentario','Contenido', 'usuario', 'categoria', 'imagen']
        widgets = {
            'nombre':forms.TextInput(attrs={'class': 'form-control ', 'placeholder':'Nombre',}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'Precio'}),
            'Contenido':forms.Textarea(attrs={'class': 'form-group', 'placeholder':'Contenido'}),
            'comentario': forms.TextInput(attrs={'class': 'form-control ', 'placeholder':'Comentario'}),
            'usuario':forms.Select(attrs={'class': 'form-control','placeholder':'Comentario'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
        }

        labels = {'nombre':'','precio':'', 'comentario':'', 'Contenido':''}
