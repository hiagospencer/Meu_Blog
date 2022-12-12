from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Blog



#Blog inicial
class BlogListView(ListView):
    template_name = 'index.html'
    model = Blog
    


#Página com somente conteudo relacionados ao cinema
class CinemaListView(ListView):
    template_name = 'cinema.html'
    model = Blog

    def get_context_data(self, **kwargs):
        context = super(CinemaListView, self).get_context_data(**kwargs)
        categoria_cinema = Blog.objects.filter(categoria='cinema')
        context['categoria_cinema'] = categoria_cinema
        return context



# Página com  conteudos relacionados a tecnologia e jogos
class TecnologiaListView(ListView):
    template_name = 'tecnologia_jogos.html'
    model = Blog

    def get_context_data(self, **kwargs):
        context = super(TecnologiaListView, self).get_context_data(**kwargs)
        categoria_tecnologia = Blog.objects.filter(categoria='tecnologia')
        context['categoria_tecnologia'] = categoria_tecnologia
        return context


# Página Relacionados a conteudos de Esportes
class EsportesListView(ListView):
    template_name = 'esportes.html'
    model = Blog

    def get_context_data(self, **kwargs):
        context = super(EsportesListView, self).get_context_data(**kwargs)
        categoria_esportes = Blog.objects.filter(categoria='esportes')
        context['categoria_esportes'] = categoria_esportes
        return context


# Página relacionado a Financia
class FinanciaListView(ListView):
    template_name = 'financas.html'
    model = Blog

    def get_context_data(self, **kwargs):
        context = super(FinanciaListView, self).get_context_data(**kwargs)
        categoria_financia = Blog.objects.filter(categoria='finanças')
        context['categoria_financia'] = categoria_financia
        return context



# Página de Detalhes dos posts
class BlogDetailView(DetailView):
    template_name = 'detalhes.html'
    model = Blog