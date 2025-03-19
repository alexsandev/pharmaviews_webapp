from django.urls import path
from marketing.views import gestao_de_verbas

urlpatterns = [
    path('', gestao_de_verbas, name='gestao-de-verbas'),
]