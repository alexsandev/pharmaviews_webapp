import datetime
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from marketing.models import Acao


class AcaoForm(forms.ModelForm):
        
        def clean_data_prevista(self):
            data = self.cleaned_data['data_prevista']

            if data < datetime.date.today():
                raise ValidationError(_('Você não pode selecionar uma data no passado.'))

            if data < datetime.date.today() + datetime.timedelta(days=10):
                raise ValidationError(_('A data do evento precisa ser no minimo em 10 dias.'))

            return data
        
        def clean_investimento(self):
             valor = self.cleaned_data['investimento']

             if valor <= 0:
                  raise ValidationError(_('O valor investido na ação não pode ser menor ou igual a zero.'))
             
             return valor
        
        class Meta:
            model = Acao
            fields = ['codigo_acao', 'data_prevista', 'investimento']
            widgets = {
                'codigo_acao': forms.Select(attrs={'class': 'form-control'}),
                "data_prevista": forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
                'investimento': forms.NumberInput(attrs={'class': 'form-control'}),
            }
                
