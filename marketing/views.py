from django.shortcuts import render

def gestao_de_verbas(request):
    context = {'mensagem': 'Hello World!'}
    return render(request, 'marketing/gestao_de_verbas.html', context)
