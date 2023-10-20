from rest_framework import serializers
from .models import Empresa, Monedas, TipoComprobantes, ComprobanteConfig, Impuesto

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'

class MonedasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monedas
        fields = '__all__'

class TipoComprobantesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoComprobantes
        fields = '__all__'

class ComprobanteConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComprobanteConfig
        fields = '__all__'

class ImpuestoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Impuesto
        fields = '__all__'