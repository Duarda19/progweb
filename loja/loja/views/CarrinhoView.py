from django.shortcuts import render, get_object_or_404, redirect
from loja.models import Produto, Carrinho, CarrinhoItem, Usuario
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.utils import timezone


# Função para adicionar um item ao carrinho
def create_carrinhoitem_view(request, produto_id=None):
    print('create_carrinhoitem_view')
    produto = get_object_or_404(Produto, pk=produto_id)

    if produto:
        print('produto: ' + str(produto.id))

    # Tenta pegar o carrinho da sessão ou cria um novo carrinho
    carrinho_id = request.session.get('carrinho_id')
    print('carrinho: ' + str(carrinho_id))
    carrinho = None

    if carrinho_id:
        # Se o carrinho já estiver na sessão, tentamos obter o carrinho
        carrinho = Carrinho.objects.filter(id=carrinho_id).first()
        print(carrinho)

        if carrinho:
            print('carrinho1: ' + str(carrinho.id))
            hoje = datetime.today().date()
            # Caso queira definir uma expiração do carrinho
            if carrinho.criado_em.date() != hoje:
                # Se o carrinho não for de hoje, cria um novo carrinho
                carrinho = Carrinho.objects.create()
                # Armazena o ID do carrinho na sessão
                request.session['carrinho_id'] = carrinho.id
                print('novo carrinho: ' + str(carrinho.id))
        else:
            # Se o carrinho não existir na sessão, cria um novo carrinho
            carrinho = Carrinho.objects.create()
            request.session['carrinho_id'] = carrinho.id
            print('carrinho2: ' + str(carrinho.id))
    else:
        # Se o carrinho não existir na sessão, cria um novo carrinho
        carrinho = Carrinho.objects.create()
        request.session['carrinho_id'] = carrinho.id
        print('carrinho2: ' + str(carrinho.id))

    # Verifica se o produto já existe no carrinho do usuário
    carrinho_item = CarrinhoItem.objects.filter(carrinho=carrinho, produto=produto).first()

    if carrinho_item:
        # Se o produto já estiver no carrinho, apenas aumenta a quantidade
        carrinho_item.quantidade += 1
        print('item de carrinho: Acrescentou 1 item do produto ' + str(carrinho_item.id))
    else:
        # Se o produto não estiver no carrinho, cria um novo item no carrinho
        carrinho_item = CarrinhoItem.objects.create(
            carrinho=carrinho,
            produto=produto,
            quantidade=1,
            preco=produto.preco
        )
        print('item de carrinho: Acrescentou o produto ' + str(carrinho_item.id))

    carrinho_item.save()
    print('item de carrinho salvo: ' + str(carrinho_item.id))

    return redirect('/carrinho')


# Função para listar os itens do carrinho
def list_carrinho_view(request):
    print('list_carrinho_view')
    carrinho = None

    # Tenta pegar o carrinho da sessão ou cria um novo carrinho
    carrinho_id = request.session.get('carrinho_id')
    if carrinho_id:
        print('carrinho: ' + str(carrinho_id))

        # Obtém o carrinho do usuário
        carrinho = Carrinho.objects.filter(id=carrinho_id).first()
        if carrinho:
            print('Data do carrinho: ' + str(carrinho.criado_em))

        # Verifica se há itens no carrinho do usuário
        carrinho_item = CarrinhoItem.objects.filter(carrinho_id=carrinho_id)
        if carrinho_item:
            print('itens de carrinho encontrado: ' + str(carrinho_item))
        
        # Contexto para renderizar o template
        context = {
            'carrinho': carrinho,
            'itens': carrinho_item
        }
        return render(request, 'carrinho/carrinho-listar.html', context=context)
# Função para confirmar a compra, login obrigatório
@login_required
def confirmar_carrinho_view(request):
    print('confirmar_carrinho_view')
    carrinho = None

    # Tenta pegar o carrinho da sessão ou cria um novo carrinho
    carrinho_id = request.session.get('carrinho_id')
    if carrinho_id:
        print('carrinho: ' + str(carrinho_id))
        # Obtém o carrinho do usuário
        carrinho = Carrinho.objects.filter(id=carrinho_id).first()

        # Obtém o usuário
        usuario = get_object_or_404(Usuario, user=request.user)
        print('Usuario: ' + str(usuario))

        if usuario:
            carrinho.user_id = usuario.id
            carrinho.situacao = 1
            carrinho.confirmado_em = timezone.make_aware(datetime.today())
            carrinho.save()
            print('carrinho salvo')

    context = {
        'carrinho': carrinho
    }
    return render(request, 'carrinho/carrinho-confirmado.html', context=context)


def remover_item_view(request, item_id):
    item = get_object_or_404(CarrinhoItem, id=item_id)
    # Verifica se o item pertence ao carrinho do usuário (opcional)
    carrinho_id = request.session.get('carrinho_id')
    if carrinho_id == item.carrinho.id:
        item.delete()
    return redirect('/carrinho')




