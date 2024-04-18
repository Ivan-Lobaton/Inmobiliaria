from django.urls import path
from inmobiliaria_app.api.views import EdificiosAV, EdificiosDetalleAV, CasasAV, CasasDetalleAV, FincasAV, FincasDetalleAV, PropietariosAV, PropietariosDetalleAV

urlpatterns = [
    path('edificios/', EdificiosAV.as_view(), name='edificios-list'),
    path('edificios/<int:pk>', EdificiosDetalleAV.as_view(), name='edificios-detalles'),
    
    path('casas/', CasasAV.as_view(), name='edificios-list'),
    path('casas/<int:pk>', CasasDetalleAV.as_view(), name='edificios-detalles'),
    
    path('fincas/', FincasAV.as_view(), name='edificios-list'),
    path('fincas/<int:pk>', FincasDetalleAV.as_view(), name='edificios-detalles'),
    
    path('propietarios/', PropietariosAV.as_view(), name='edificios-list'),
    path('propietarios/<int:pk>', PropietariosDetalleAV.as_view(), name='edificios-detalles'),
]
