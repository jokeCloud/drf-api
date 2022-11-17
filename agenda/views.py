from django.http import JsonResponse
from django.shortcuts import get_object_or_404  # render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from agenda.models import Agendamento
from agenda.serializers import AgendamentoSerializer


# listar, alterar e deletar agendamento
@api_view(http_method_names=['GET', 'PATCH', 'DELETE'])
def agendamento_detail(request, id):
    obj = get_object_or_404(Agendamento, id=id)
    if request.method == 'GET':
        serializer = AgendamentoSerializer(obj)
        return JsonResponse(serializer.data)
    if request.method == 'PATCH':
        serializer = AgendamentoSerializer(
            obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)
    if request.method == 'DELETE':
        obj.delete()
        return Response(status=204)


# listar e inserir agendamentos
@api_view(http_method_names=['GET', 'POST'])
def agendamento_list(request):
    if request.method == 'GET':
        qs = Agendamento.objects.all()
        serializer = AgendamentoSerializer(qs, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == 'POST':
        data = request.data  # {"nome_cliente": "João"...}
        serializer = AgendamentoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
