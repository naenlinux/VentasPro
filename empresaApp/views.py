from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import Empresa, Monedas, TipoComprobantes, ComprobanteConfig, Impuesto
from .serializers import EmpresaSerializer, MonedasSerializer, TipoComprobantesSerializer, ComprobanteConfigSerializer, ImpuestoSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class EmpresaViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = Empresa.objects.all().order_by('-id')
    serializer_class = EmpresaSerializer

    def create(self, request):
        serializer = EmpresaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    '''def list(self, request):
        serializer = EmpresaSerializer(self.queryset, many=True)
        return Response(serializer.data)'''


class MonedaViewset(viewsets.ModelViewSet):
    queryset = Monedas.objects.all().order_by('id')
    serializer_class = MonedasSerializer

class TipoComprobantesViewset(viewsets.ModelViewSet):
    #TipoComprobantes.objects.all().delete()
    queryset = TipoComprobantes.objects.all().order_by('id')
    serializer_class = TipoComprobantesSerializer

class ComprobanteConfigViewset(viewsets.ModelViewSet):
    queryset = ComprobanteConfig.objects.all().order_by('id')
    serializer_class = ComprobanteConfigSerializer

class ImpuestoViewset(viewsets.ModelViewSet):
    queryset = Impuesto.objects.all()
    serializer_class = ImpuestoSerializer
#class ImageUploadView(API)