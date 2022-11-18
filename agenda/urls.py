from django.urls import path

from agenda.views import AgendamentoDetail, AgendamentoList

urlpatterns = [
    path('agendamentos/', AgendamentoList.as_view(), name='agendamento_list'),
    path('agendamentos/<int:id>', AgendamentoDetail.as_view(), name='agendamento_detail'),  # noqa
]
