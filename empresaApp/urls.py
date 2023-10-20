from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'empresa',views.EmpresaViewSet)
router.register(r'moneda',views.MonedaViewset)
router.register(r'tipocomprobante',views.TipoComprobantesViewset)
router.register(r'comprobanteconfig',views.ComprobanteConfigViewset)
router.register(r'impuesto',views.ImpuestoViewset)

urlpatterns = [
    path('',include(router.urls)),
]

