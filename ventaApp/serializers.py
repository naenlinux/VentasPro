from rest_framework import serializers
from .models import Pedidos,PedidosDetalle,Ventas

class PedidosSerializer(serializers.ModelSerializer):
    usuario = serializers.CharField(source='idUsuario.username', read_only=True)
    comprobante = serializers.CharField(source='idComprob.nombre', read_only=True)
    moneda = serializers.CharField(source='idMoneda.nombre', read_only=True)
    class Meta:
        model = Pedidos
        fields = '__all__'
    
class PedidosDetalleSerializer(serializers.ModelSerializer):
    proporcionUM = serializers.CharField(source='idAlmacen.idProducto.unidadMedida.proporcion',read_only=True)
    class Meta:
        model = PedidosDetalle
        fields = '__all__'

class VentasSerializer(serializers.ModelSerializer):
    subtotal = serializers.CharField(source='idPedido.subtotal',read_only=True)
    igv_total = serializers.CharField(source='idPedido.igv_total',read_only=True)
    comprobante = serializers.CharField(source='tipComprobante.nombre',read_only=True)
    comprobante_cod = serializers.CharField(source='tipComprobante.codigoSunat',read_only=True)
    numPedido = serializers.CharField(source='idPedido.numero',read_only=True)
    fechaPedido = serializers.CharField(source='idPedido.fecha',read_only=True)
    cliente = serializers.CharField(source='idPedido.cliente',read_only=True)
    vendedor = serializers.CharField(source='idPedido.idUsuario.username',read_only=True)
    moneda = serializers.CharField(source='idPedido.idMoneda.nombre',read_only=True)
    
    class Meta:
        model = Ventas
        fields = '__all__'

class CajaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ventas
        fields = '__all__'