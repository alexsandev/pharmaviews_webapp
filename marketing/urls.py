from django.urls import path
from marketing.views import gestao_de_verbas, adicionar_acao

urlpatterns = [
    path('', gestao_de_verbas, name='gestao-de-verbas'),
    path('adicionar/', adicionar_acao, name='adicionar-acao'),
]