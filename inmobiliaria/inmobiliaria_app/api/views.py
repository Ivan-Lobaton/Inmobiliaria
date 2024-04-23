from django.shortcuts import render
from django.http import HttpResponseRedirect
from rest_framework.response import Response
from inmobiliaria_app.admin import Edificios, Casas, Fincas, Propietarios
from inmobiliaria_app.api.serializers import EdificioSerializer, CasasSerializer, FincasSerializer, PropietariosSerializer

from rest_framework.views import APIView
from rest_framework import status
from inmobiliaria_app.models import Edificios, Casas, Fincas, Propietarios
from inmobiliaria_app.api.forms import EdificiosForm, CasasForm, FincasForm, PropietariosForm

class EdificiosLiveView(APIView):
    def get(self, request):
        edificios = Edificios.objects.all()
        serializer = EdificioSerializer(edificios, many=True)
        return render(request, 'edificios.html', {'edificios': serializer.data})
    
class EdificiosCreateView(APIView):
    def get(self, request):
        form = EdificiosForm()
        return render(request, 'crear_edificio.html', {'form': form})
    
    def post(self, request):
        form = EdificiosForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/portal/edificios/')
        return render(request, 'crear_edificio.html', {'form': form})
    
class CasasLiveView(APIView):
    def get(self, request):
        casas = Casas.objects.all()
        serializer = CasasSerializer(casas, many=True)
        return render(request, 'casas.html', {'casas': serializer.data})
    
class CasasCreateView(APIView):
    def get(self, request):
        form = CasasForm()
        return render(request, 'crear_casa.html', {'form': form})
    
    def post(self, request):
        form = CasasForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/portal/casas/')
        return render(request, 'crear_casa.html', {'form': form})
    
class FincasLiveView(APIView):
    def get(self, request):
        fincas = Fincas.objects.all()
        serializer = FincasSerializer(fincas, many=True)
        return render(request, 'fincas.html', {'fincas': serializer.data})
    
class FincasCreateView(APIView):
    def get(self, request):
        form = FincasForm()
        return render(request, 'crear_finca.html', {'form': form})
    
    def post(self, request):
        form = FincasForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/portal/fincas/')
        return render(request, 'crear_finca.html', {'form': form})
    
class PropietariosLiveView(APIView):
    def get(self, request):
        propietarios = Propietarios.objects.all()
        serializer = PropietariosSerializer(propietarios, many=True)
        return render(request, 'propietarios.html', {'propietarios': serializer.data})
    
class PropietariosCreateView(APIView):
    def get(self, request):
        form = PropietariosForm()
        return render(request, 'crear_propietario.html', {'form': form})
    
    def post(self, request):
        form = PropietariosForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/portal/propietarios/')
        return render(request, 'crear_propietario.html', {'form': form})