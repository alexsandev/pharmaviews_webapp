from django.urls import path
from marketing.views import AcaoUpdate, gestao_de_verbas, AcaoDelete

urlpatterns = [
    path('', gestao_de_verbas, name='gestao-de-verbas'),
    path('delete/<int:pk>/', AcaoDelete.as_view(), name='acao-delete'),
    path('update/<int:pk>/', AcaoUpdate.as_view(), name='acao-update'),
]