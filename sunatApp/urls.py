from django.urls import path, include
from rest_framework import routers
from .views import Sunat

router = routers.DefaultRouter()
#router.register(r'enviarsunat', enviarSunat.as_view(), name='enviar_sunat')


urlpatterns = [
    path('', include(router.urls)),
    path('sunat/', Sunat.as_view(), name='sunat')
]