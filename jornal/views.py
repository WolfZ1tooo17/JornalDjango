from django.shortcuts import render, get_object_or_404, redirect
from .models import Artigo, Comentario

def lista_artigos(request):
    artigos = Artigo.objects.all().order_by('-data_publicacao')
    return render(request, 'jornal/lista_artigos.html', {'artigos': artigos})

def detalhe_artigo(request, artigo_id):
    artigo = get_object_or_404(Artigo, pk=artigo_id)
    return render(request, 'jornal/detalhe_artigo.html', {'artigo': artigo})
    artigo.visualizacoes += 1
    artigo.save()


def comentarios_artigo(request, artigo_id):
    artigo = get_object_or_404(Artigo, pk=artigo_id)
    if request.method == 'POST':
        texto = request.POST.get('texto')
        if texto:
            Comentario.objects.create(artigo=artigo, texto=texto)
            return redirect('comentarios_artigo', artigo_id=artigo.id)
    
    comentarios = artigo.comentarios.all().order_by('-data_publicacao')
    return render(request, 'jornal/comentarios_artigo.html', {
        'artigo': artigo,
        'comentarios': comentarios
    })
