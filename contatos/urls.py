from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('busca/', views.busca, name='busca'),
    path('contato/<int:contato_id>', views.ver_contato, name='contato'),
    
    
]