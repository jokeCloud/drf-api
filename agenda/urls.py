from django.urls import path

from agenda.views import AgendamentoDetail, AgendamentoList, PrestadorList

urlpatterns = [
    path('agendamentos/', AgendamentoList.as_view(), name='agendamento_list'),
    path('agendamentos/<int:pk>', AgendamentoDetail.as_view(), name='agendamento_detail'),  # noqa
    path('prestadores/', PrestadorList.as_view(), name='prestador_list')
]
