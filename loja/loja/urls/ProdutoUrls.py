from django.urls import path
from loja.views.ProdutoView import list_produto_view, edit_produto_view, edit_produto_postback
urlpatterns = [
    path("", list_produto_view, name='produto'),
    path("<int:id>", list_produto_view, name='produto'),
    path("edit/<int:id>", edit_produto_view, name= 'edit_produto'),
    path("edit", edit_produto_postback, name= 'edit_produto_postback'),
]