from django.contrib import admin
from inmobiliaria_app.models import Edificios, Casas, Fincas, Propietarios

# Register your models here.
admin.site.register(Edificios)
admin.site.register(Casas)
admin.site.register(Fincas)
admin.site.register(Propietarios)