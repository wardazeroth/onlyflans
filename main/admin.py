from django.contrib import admin
from main.models import Contacto, Flan

class ContactoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Contacto, ContactoAdmin)
# Register your models here.

class FlanAdmin(admin.ModelAdmin):
    pass
admin.site.register(Flan, FlanAdmin)
# Register your models here.