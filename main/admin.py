from django.contrib import admin
from main.models import Persona

class PersonaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Persona, PersonaAdmin)
# Register your models here.
