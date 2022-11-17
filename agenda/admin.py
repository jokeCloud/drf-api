from django.contrib import admin

from agenda.models import Agendamento


# admin.site.register(Agendamento)
@admin.register(Agendamento)
class AgendamentoADmin(admin.ModelAdmin):
    list_display = ('nome_cliente', 'email_cliente', 'data_horario')
