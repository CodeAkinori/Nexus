from django.db import models
from django.contrib.auth.models import User

class Topico(models.Model):
    titulo = models.CharField(max_length=255)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'forum'

class Post(models.Model):
    topico = models.ForeignKey(Topico, on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    conteudo = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'forum'

