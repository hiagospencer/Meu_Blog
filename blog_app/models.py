from django.db import models
from django.utils import timezone


class Blog(models.Model):
    titulo = models.CharField(max_length=1000)
    mini_descricao = models.TextField(max_length=2000, default=False)
    descricao = models.TextField(max_length=1000000)
    image = models.ImageField(upload_to='thumb_img')
    data = models.DateTimeField(default=timezone.now)
    autor = models.CharField(max_length=30)

    def __str__(self):
        return self.titulo


