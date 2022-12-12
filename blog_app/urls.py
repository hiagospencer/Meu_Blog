from django.urls import path
from blog_app.views import (BlogListView, BlogDetailView,CinemaListView,
                    TecnologiaListView, EsportesListView,FinancasListView,
)

app_name = 'blog_app'

urlpatterns = [ 
    path('', BlogListView.as_view(), name='blog'),
    path('detalhe/<int:pk>', BlogDetailView.as_view(), name='detalhes'),
    path('cinema/', CinemaListView.as_view(), name='cinema'),
    path('tecnologia/', TecnologiaListView.as_view(), name='tecnologia'),
    path('esportes/', EsportesListView.as_view(), name='sports'),
    path('financas/', FinancasListView.as_view(), name='financas'),
]