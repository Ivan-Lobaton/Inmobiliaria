from rest_framework import serializers
from inmobiliaria_app.models import Edificios, Casas, Fincas, Propietarios

class EdificioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Edificios
        fields = '__all__'

class CasasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Casas
        fields = '__all__'

class FincasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fincas
        fields = '__all__'

class PropietariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Propietarios
        fields = '__all__'
