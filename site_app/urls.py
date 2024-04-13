from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('pesquisar/', views.pesquisar, name="pesquisar"), 
    
    path('criar/', views.criar, name="criar"), 
    
    path('deletar/<int:id>', views.deletar, name="deletar_id"),
    path('deletar/', views.deletar, name="deletar"),
    
    path('atualizar/<int:id>', views.atualizar, name="atualizar_id"),
    path('atualizar/', views.atualizar, name="atualizar"),

]
