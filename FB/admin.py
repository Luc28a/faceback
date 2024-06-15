from django.contrib import admin
from .models import Muntu

# Register your models here.

class Surveillance(admin.ModelAdmin):
    list_display = ('nom','mot_de_passe')


admin.site.register(Muntu, Surveillance)