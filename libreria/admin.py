from django.contrib import admin
from .models import *

# Register your models here.

class libroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tipo', 'descripcion')
    list_filter = ('tipo',)

admin.site.register(libro, libroAdmin)