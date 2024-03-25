from django.contrib import admin

# Register your models here.
from django.contrib import admin #isso já vai estar existindo no arquivo
# Register your models here.
from .models import * #imporata nossos models
admin.site.register(Fabricante) #adiciona a interface do adm
from django.contrib import admin #isso já vai estar existindo no arquivo
admin.site.register(Categoria)
admin.site.register(Produto)

