from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Blog



#Blog inicial
class BlogListView(ListView):
    template_name = 'index.html'
    model = Blog
    paginate_by = 10
    
    def get_context_data(self, **kwargs):
        context = super(BlogListView, self).get_context_data(**kwargs)
        post_blog = Blog.objects.order_by('-data')
        context["post_blog"] = post_blog
        return context

    
#Página com somente conteudo relacionados ao cinema
class CinemaListView(ListView):
    template_name = 'cinema.html'
    model = Blog
    paginate_by = 10
    

    def get_context_data(self, **kwargs):
        context = super(CinemaListView, self).get_context_data(**kwargs)
        categoria_cinema = Blog.objects.filter(categoria='cinema').order_by('-data')
        context['categoria_cinema'] = categoria_cinema
        return context



# Página com  conteudos relacionados a tecnologia e jogos
class TecnologiaListView(ListView):
    template_name = 'tecnologia_jogos.html'
    model = Blog

    def get_context_data(self, **kwargs):
        context = super(TecnologiaListView, self).get_context_data(**kwargs)
        categoria_tecnologia = Blog.objects.filter(categoria='tecnologia').order_by('-data')
        context['categoria_tecnologia'] = categoria_tecnologia
        return context


# Página Relacionados a conteudos de Esportes
class EsportesListView(ListView):
    template_name = 'esportes.html'
    model = Blog

    def get_context_data(self, **kwargs):
        context = super(EsportesListView, self).get_context_data(**kwargs)
        categoria_esportes = Blog.objects.filter(categoria='esportes').order_by('-data')
        context['categoria_esportes'] = categoria_esportes
        return context


# Página relacionado a Financia
class FinancasListView(ListView):
    template_name = 'financas.html'
    model = Blog

    def get_context_data(self, **kwargs):
        context = super(FinancasListView, self).get_context_data(**kwargs)
        categoria_financas = Blog.objects.filter(categoria='finanças').order_by('-data')
        context['categoria_financas'] = categoria_financas
        return context



# Página de Detalhes dos posts
class BlogDetailView(DetailView):
    template_name = 'detalhes.html'
    model = Blog


