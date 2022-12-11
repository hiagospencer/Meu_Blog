from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

LISTA_CATEGORIA = (
    ('esportes', 'Esportes'),
    ('noticias', 'Notícias'),
    ('cinema', 'Cinema'), 
    ('tecnologia', 'Tecnologia'),
    ('finanças', 'Finanças'),
    
)
class Blog(models.Model):
    titulo = models.CharField(max_length=1000)
    mini_descricao = models.CharField(max_length=2000)
    descricao = RichTextField(max_length=1000000)
    image = models.ImageField(upload_to='thumb_img')
    data = models.DateTimeField(default=timezone.now)
    autor = models.CharField(max_length=30)
    categoria = models.CharField(max_length=30, choices=LISTA_CATEGORIA)

    def __str__(self):
        return self.titulo


