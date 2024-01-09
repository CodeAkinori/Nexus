from django.shortcuts import render, get_object_or_404
from .models import Topico, Post

def lista_topicos(request):
    topicos = Topico.objects.all()
    return render(request, 'forum/lista_topicos.html', {'topicos': topicos})

def detalhes_topico(request, topico_id):
    topico = get_object_or_404(Topico, pk=topico_id)
    posts = Post.objects.filter(topico=topico)
    return render(request, 'forum/detalhes_topico.html', {'topico': topico, 'posts': posts})

def criar_post(request, topico_id):
    topico = get_object_or_404(Topico, pk=topico_id)

    if request.method == 'POST':
        conteudo = request.POST['conteudo']
        # Aqui você precisa adicionar lógica para criar o post no banco de dados
        # Exemplo: Post.objects.create(tópico=tópico, autor=request.user, conteúdo=conteúdo)
        # Certifique-se de lidar com a lógica de criação de post e redirecionamento corretamente

    return render(request, 'forum/criar_post.html', {'topico': topico})