from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Blog


def blog(request):
    return render(request, 'index.html')

class BlogListView(ListView):
    template_name = 'index.html'
    model = Blog


class BlogDetailView(DetailView):
    template_name = 'detalhes.html'
    model = Blog