from rest_framework.response import Response
from inmobiliaria_app.admin import Edificios, Casas, Fincas, Propietarios
from inmobiliaria_app.api.serializers import EdificioSerializer, CasasSerializer, FincasSerializer, PropietariosSerializer

from rest_framework.views import APIView
from rest_framework import status

class EdificiosAV(APIView):
    def get(self, request):
        edificios = Edificios.objects.all()
        serializer = EdificioSerializer(edificios, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = EdificioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EdificiosDetalleAV(APIView):
    def get(self, request, pk):
        try:
            edificios = Edificios.objects.get(pk=pk)
        except Edificios.DoesNotExist:
            return Response({'error': 'Edificio no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = EdificioSerializer(edificios, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        try:
            edificios = Edificios.objects.get(pk=pk)
        except Edificios.DoesNotExist:
            return Response({'error': 'Edificio no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = EdificioSerializer(edificios, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            edificios = Edificios.objects.get(pk=pk)
        except Edificios.DoesNotExist:
            return Response({'error': 'Edificio no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        edificios.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CasasAV(APIView):
    def get(self, request):
        casas = Casas.objects.all()
        serializer = CasasSerializer(casas, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = CasasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CasasDetalleAV(APIView):
    def get(self, request, pk):
        try:
            casas = Casas.objects.get(pk=pk)
        except Casas.DoesNotExist:
            return Response({'error': 'Casa no encontrada'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CasasSerializer(casas, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        try:
            casas = Casas.objects.get(pk=pk)
        except Casas.DoesNotExist:
            return Response({'error': 'Casa no encontrada'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CasasSerializer(casas, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            casas = Casas.objects.get(pk=pk)
        except Casas.DoesNotExist:
            return Response({'error': 'Casa no encontrada'}, status=status.HTTP_404_NOT_FOUND)
        
        casas.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class FincasAV(APIView):
    def get(self, request):
        fincas = Fincas.objects.all()
        serializer = FincasSerializer(fincas, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = FincasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FincasDetalleAV(APIView):
    def get(self, request, pk):
        try:
            fincas = Fincas.objects.get(pk=pk)
        except Fincas.DoesNotExist:
            return Response({'error': 'Finca no encontrada'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = FincasSerializer(fincas, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        try:
            fincas = Fincas.objects.get(pk=pk)
        except Fincas.DoesNotExist:
            return Response({'error': 'Finca no encontrada'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = FincasSerializer(fincas, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            fincas = Fincas.objects.get(pk=pk)
        except Fincas.DoesNotExist:
            return Response({'error': 'Finca no encontrada'}, status=status.HTTP_404_NOT_FOUND)
        
        fincas.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PropietariosAV(APIView):
    def get(self, request):
        propietarios = Propietarios.objects.all()
        serializer = PropietariosSerializer(propietarios, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = PropietariosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PropietariosDetalleAV(APIView):
    def get(self, request, pk):
        try:
            propietarios = Propietarios.objects.get(pk=pk)
        except Propietarios.DoesNotExist:
            return Response({'error': 'Propietario no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = PropietariosSerializer(propietarios, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        try:
            propietarios = Propietarios.objects.get(pk=pk)
        except Propietarios.DoesNotExist:
            return Response({'error': 'Propietario no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = PropietariosSerializer(propietarios, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            propietarios = Propietarios.objects.get(pk=pk)
        except Propietarios.DoesNotExist:
            return Response({'error': 'Propietario no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        propietarios.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    