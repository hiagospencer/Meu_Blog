from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Blog



#Blog inicial
class BlogListView(ListView):
    template_name = 'index.html'
    model = Blog
    paginate_by = 5
    
    def get_context_data(self, **kwargs):
        context = super(BlogListView, self).get_context_data(**kwargs)
        post_blog = Blog.objects.order_by('-data')
        context["post_blog"] = post_blog

        paginator = context['paginator']
        page_numbers_range = 5  # Display 5 page numbers
        max_index = len(paginator.page_range)

        page = self.request.GET.get('page')
        current_page = int(page) if page else 1

        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range
        if end_index >= max_index:
            end_index = max_index

        page_range = paginator.page_range[start_index:end_index]
        context['page_range'] = page_range

        return context

    
#Página com somente conteudo relacionados ao cinema
class CinemaListView(ListView):
    template_name = 'cinema.html'
    model = Blog
    

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


