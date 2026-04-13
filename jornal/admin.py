from django.contrib import admin
from .models import Artigo, Comentario, Categoria

admin.site.register(Artigo)
admin.site.register(Comentario)
admin.site.register(Categoria)