from django.shortcuts import render
from .models import Produto
from django.contrib.auth.decorators import user_passes_test

def tela_inicio(request):
    produtos = Produto.objects.all()
    return render(request, 'telas/index.html', {'produtos': produtos})


def user_is_staff(user):
    return user.is_staff


@user_passes_test(user_is_staff)
def cad_item(request):
    produtos = Produto.objects.all()
    if request.method == 'POST':
        novo_produto = Produto()
        novo_produto.nome = request.POST.get('nome')
        novo_produto.descricao = request.POST.get('descricao')
        novo_produto.imagem = request.FILES.get('imagem')
        novo_produto.save()

        produtos = {
            'produtos': Produto.objects.all()
        }

    return render(request, 'telas/cadastro_itens.html')

@user_passes_test(user_is_staff)
def excluir_item(request):
    if request.method == 'POST':
        id_item_excluir = request.POST.get('id_item')
        if id_item_excluir:
            Produto.objects.filter(id=int(id_item_excluir)).delete()
    
    produtos = Produto.objects.all()
    return render(request, 'telas/excluir_itens.html', {'produtos': produtos})

