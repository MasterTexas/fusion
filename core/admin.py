from django.contrib import admin
from .models import Servico, Cargo, Colaborador, Caracteristica, Preco

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'ativo', 'criado', 'modificado')
    search_fields = ('cargo',)

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('servico', 'descricao', 'icone', 'criado', 'modificado')

@admin.register(Colaborador)
class ColaboradorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo')
    search_fields = ('nome',)

@admin.register(Caracteristica)
class CaracteristicaAdmin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(Preco)
class PrecoAdmin(admin.ModelAdmin):
    list_display = ('servico', 'ativo', 'criado', 'modificado')
