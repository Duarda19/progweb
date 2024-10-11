from django.contrib import admin

# Register your models here.
from django.contrib import admin #isso já vai estar existindo no arquivo
# Register your models here.
from .models import * #imporata nossos models
class FabricanteAdmin(admin.ModelAdmin):
# Cria um filtro de hierarquia com datas
    date_hierarchy = 'criado_em'

class ProdutoAdmin(admin.ModelAdmin):
    date_hierarchy = 'criado_em'
    list_display = ('Produto', 'destaque', 'promocao', 'msgPromocao', 'preco', 'categoria',)
    empty_value_display = 'Vazio'
    fields = ('Produto', 'destaque', 'promocao', 'msgPromocao', 'preco', 'categoria',)
    search_fields = ('Produto',)

admin.site.register(Fabricante,FabricanteAdmin) #adiciona a interface do adm
admin.site.register(Categoria)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Usuario)

