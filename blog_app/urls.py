from django.urls import path
from blog_app.views import BlogListView, BlogDetailView

app_name = 'blog_app'

urlpatterns = [ 
    path('', BlogListView.as_view(), name='blog'),
    path('detalhe/<int:pk>', BlogDetailView.as_view(), name='detalhes'),
]