from django.urls import path
from . import views

urlpatterns = [
    path('comprobante/<int:idVenta>',views.generar_pdf, name='comprobante'),
    path('almacenexcel/',views.export_to_excel, name='almacenexcel')
]
