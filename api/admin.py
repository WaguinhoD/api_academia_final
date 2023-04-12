from django.contrib import admin

# Register your models here.
from .models import Instrutor, Plano, Programa


@admin.register(Instrutor)
class InstrutorAdmin(admin.ModelAdmin):
    list_display = ("nome", "slug_name", "sobrenome")
    prepopulated_fields = {"slug_name": ("nome", "sobrenome",)}


@admin.register(Plano)
class PlanoAdmin(admin.ModelAdmin):
    list_display = ("nome_plano", "valor")


@admin.register(Programa)
class ProgramaAdmin(admin.ModelAdmin):
    list_display = ("nome_programa",)