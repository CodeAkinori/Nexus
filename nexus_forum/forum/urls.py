from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_topicos, name='lista_topicos'),
    path('topico/<int:topico_id>/', views.detalhes_topico, name='detalhes_topico'),
    path('topico/<int:topico_id>/criar_post/', views.criar_post, name='criar_post'),
]