import datetime
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView


from marketing.forms import AcaoForm
from marketing.models import Acao

def gestao_de_verbas(request):
    acoes = Acao.objects.all()
    form = AcaoForm(initial={'data_prevista': datetime.date.today() + datetime.timedelta(days=10), 'investimento': 0})

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
            return render(request, 'marketing/gestao_de_verbas.html', {'acoes': acoes, 'form': form})
    else:
        return render(request, 'marketing/gestao_de_verbas.html', {'acoes': acoes, 'form': form})
    
class AcaoDelete(DeleteView):
    model = Acao
    success_url = reverse_lazy('gestao-de-verbas')

class AcaoUpdate(UpdateView):
    model = Acao
    form_class = AcaoForm
    success_url = reverse_lazy('gestao-de-verbas')

def erro_no_servidor(request):
    render(request, '500.html', status=500)