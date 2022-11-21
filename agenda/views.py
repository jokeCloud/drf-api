# from datetime import datetime, timezone
# from django.http import JsonResponse
# from django.shortcuts import get_object_or_404  # render
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework.views import APIView

from django.contrib.auth.models import User
from rest_framework import generics, permissions  # mixins

from agenda.models import Agendamento
from agenda.serializers import AgendamentoSerializer, PrestadorSerializer

"""
regras

- Qualquer cliente (autenticado ou não) seja capaz de criar um agendamento.
- Apenas o prestador de serviço pode visualizar todos os agendamnetos em sua agenda.
- Apenas o prestador de serviço pode manipular os seus agendamentos.
"""


class IsOwnerOrCreateOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        username = request.query_params.get('username', None)
        if request.user.username == username:
            return True
        return False


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.prestador == request.user:
            return True
        return False


class AgendamentoList(generics.ListCreateAPIView):
    serializer_class = AgendamentoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        username = self.request.query_params.get('username', None)
        return Agendamento.objects.filter(prestador__username=username)


# listar, alterar e deletar agendamento
class AgendamentoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer
    permission_classes = [IsOwner]


class PrestadorList(generics.ListAPIView):
    serializer_class = PrestadorSerializer
    queryset = User.objects.all()
