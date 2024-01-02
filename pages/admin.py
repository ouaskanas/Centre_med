from django.contrib import admin

# Register your models here.
from .models import *
# Register your models here.
admin.site.site_header='Healttica'
admin.site.site_title='Admin'
admin.site.register(Salle)
admin.site.register(Medecin)
admin.site.register(reservation)
admin.site.register(patient)
admin.site.register(rendezvous)
admin.site.register(FicheP)
admin.site.register(profilI)