from django.contrib import admin

from marketing.models import Acao, TipoAcao

# Register your models here.
@admin.register(Acao)
class AcaoAdmin(admin.ModelAdmin):
    pass

@admin.register(TipoAcao)
class TipoAcaoAdmin(admin.ModelAdmin):
    pass

