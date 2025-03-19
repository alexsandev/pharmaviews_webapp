from django.db import models

class Acao(models.Model):
    investimento = models.DecimalField(max_digits=14, decimal_places=2)
    data_prevista = models.DateField()
    data_cadastro = models.DateField()
    codigo_acao = models.ForeignKey('TipoAcao', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'acao'
        verbose_name = 'ação'
        verbose_name_plural = 'ações'
    
    def __str__(self):
        return f'{self.codigo_acao} ({self.data_prevista})'
        

class TipoAcao(models.Model):
    codigo_acao = models.AutoField(primary_key=True)
    nome_acao = models.CharField(max_length=100, null=False)

    class Meta:
        db_table = 'tipo_acao'
        verbose_name = 'tipo de ação'
        verbose_name_plural = "tipos de ação"

    def __str__(self):
        return self.nome_acao