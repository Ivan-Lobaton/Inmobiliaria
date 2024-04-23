from django import forms
from inmobiliaria_app.models import Edificios, Casas, Fincas, Propietarios

class EdificiosForm(forms.ModelForm):
    class Meta:
        model = Edificios
        fields = ['nombre', 'direccion', 'tipoedificio', 'estadoedificio', 'añoconstruccion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'tipoedificio': forms.Select(attrs={'class': 'form-control'}),
            'estadoedificio': forms.TextInput(attrs={'class': 'form-control'}),
            'añoconstruccion': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
class CasasForm(forms.ModelForm):
    class Meta:
        model = Casas
        fields = ['barrio', 'direccion', 'numerohabitaciones', 'añocontruccion', 'tipocontruccion']
        widgets = {
            'barrio': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'numerohabitaciones': forms.TextInput(attrs={'class': 'form-control'}),
            'añocontruccion': forms.TextInput(attrs={'class': 'form-control'}),
            'tipocontruccion': forms.Select(attrs={'class': 'form-control'}),
        }
        
class FincasForm(forms.ModelForm):
    class Meta:
        model = Fincas
        fields = ['nombre', 'tamañoterreno', 'actividad', 'infraestructura']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'tamañoterreno': forms.TextInput(attrs={'class': 'form-control'}),
            'actividad': forms.Select(attrs={'class': 'form-control'}),
            'infraestructura': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
class PropietariosForm(forms.ModelForm):
    class Meta:
        model = Propietarios
        fields = ['nombre', 'apellido', 'celular', 'cedula', 'idedificios', 'idcasas', 'idfincas']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'celular': forms.TextInput(attrs={'class': 'form-control'}),
            'cedula': forms.TextInput(attrs={'class': 'form-control'}),
            'idedificios': forms.Select(attrs={'class': 'form-control'}),
            'idcasas': forms.Select(attrs={'class': 'form-control'}),
            'idfincas': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(PropietariosForm, self).__init__(*args, **kwargs)
        self.fields['idedificios'].queryset = Edificios.objects.all()
        self.fields['idcasas'].queryset = Casas.objects.all()
        self.fields['idfincas'].queryset = Fincas.objects.all()
