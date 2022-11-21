# from datetime import datetime
from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework import serializers

from agenda.models import Agendamento


class AgendamentoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Agendamento
        fields = '__all__'
        # ['id', 'data_horario', 'nome_cliente', 'email_cliente', 'telefone_cliente', 'prestador']

    prestador = serializers.CharField()
    # validar os tipos passados -> int, str?
    # validações especificas: validate_prestador
    # validação geral (object-level) -> def validate

    def validate_prestador(self, value):
        try:
            prestador_obj = User.objects.get(username=value)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                'Username não existe!')
        return prestador_obj

    def validate_data_horario(self, value):
        if value < timezone.now():
            raise serializers.ValidationError(
                'Agendamento não pode ser feito no passado.')
        return value

    def validate(self, attrs):
        telefone_cliente = attrs.get('telefone_cliente', '')
        email_cliente = attrs.get('email_cliente', '')

        if email_cliente.endswith('.br') and telefone_cliente.startswith('+') and not telefone_cliente.startswith('+55'):  # noqa
            raise serializers.ValidationError(
                'E-mail brasileiro deve estar associado a um número de telefone do Brasil (+55).')  # noqa
        return attrs


class PrestadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'agendamentos']

    agendamentos = AgendamentoSerializer(many=True, read_only=True)
