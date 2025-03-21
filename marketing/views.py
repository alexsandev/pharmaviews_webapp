import datetime
from django.shortcuts import redirect, render

from marketing.forms import AcaoForm
from marketing.models import Acao

def gestao_de_verbas(request):
    acoes = Acao.objects.all()
    form = AcaoForm()
    context = {'acoes': acoes,'form': form}
    return render(request, 'marketing/gestao_de_verbas.html', context)

def adicionar_acao(request):
    if request.method == 'POST':
        form = AcaoForm(request.POST)
        if form.is_valid():
            acao = Acao()
            acao.codigo_acao = form.cleaned_data['codigo_acao']
            acao.data_prevista = form.cleaned_data['data_prevista']
            acao.investimento = form.cleaned_data['investimento']
            acao.data_cadastro = datetime.date.today()
            acao.save()
            return redirect('gestao-de-verbas')
        else:
            acoes = Acao.objects.all()
            return render(request, 'marketing/gestao_de_verbas.html', {'acoes': acoes, 'form': form})
    else:
        return redirect('gestao-de-verbas')