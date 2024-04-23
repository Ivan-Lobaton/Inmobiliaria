from django.urls import path
from inmobiliaria_app.api.views import EdificiosLiveView, EdificiosCreateView, CasasLiveView, CasasCreateView, FincasLiveView, FincasCreateView, PropietariosLiveView, PropietariosCreateView

urlpatterns = [
    path('edificios/', EdificiosLiveView.as_view(), name='edificios-list'),
    path('edificios/crear/', EdificiosCreateView.as_view(), name='crear_edificio'),
    path('casas/', CasasLiveView.as_view(), name='casas-list'),
    path('casas/crear/', CasasCreateView.as_view(), name='crear_casa'),
    path('fincas/', FincasLiveView.as_view(), name='fincas-list'),
    path('fincas/crear/', FincasCreateView.as_view(), name='crear_finca'),
    path('propietarios/', PropietariosLiveView.as_view(), name='propietarios-list'),
    path('propietarios/crear/', PropietariosCreateView.as_view(), name='crear_propietario'),
]