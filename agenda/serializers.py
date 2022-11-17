# from datetime import datetime

from django.utils import timezone
from rest_framework import serializers

from agenda.models import Agendamento


class AgendamentoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Agendamento
        fields = ['id', 'data_horario', 'nome_cliente',
                  'email_cliente', 'telefone_cliente']

    # data_horario = serializers.DateTimeField()  # YYYYY-MM-DDThh:mm
    # nome_cliente = serializers.CharField(max_length=200)
    # email_cliente = serializers.EmailField()
    # telefone_cliente = serializers.CharField(max_length=20)

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
