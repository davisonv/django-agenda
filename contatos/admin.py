from calendar import c
from django.contrib import admin
from .models import Categoria, Contato


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'categoria', 'telefone', 'email',)
    list_display_links = ('nome', 'sobrenome',)
    search_fields = ('nome', 'sobrenome',)
    list_per_page = 10

admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)

