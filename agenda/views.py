# from datetime import datetime, timezone

from django.http import JsonResponse
from django.shortcuts import get_object_or_404  # render
# from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from agenda.models import Agendamento
from agenda.serializers import AgendamentoSerializer


# listar, alterar e deletar agendamento
class AgendamentoDetail(APIView):
    def get(self, request):
        obj = get_object_or_404(Agendamento, id=id)
        serializer = AgendamentoSerializer(obj)
        return JsonResponse(serializer.data)

    def patch(self, request):
        obj = get_object_or_404(Agendamento, id=id)
        serializer = AgendamentoSerializer(
            obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

    def delete(self, request):
        obj = get_object_or_404(Agendamento, id=id)
        obj.delete()
        return Response(status=204)


class AgendamentoList(APIView):
    def get(self, request):
        qs = Agendamento.objects.all()
        serializer = AgendamentoSerializer(qs, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        data = request.data
        serializer = AgendamentoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
