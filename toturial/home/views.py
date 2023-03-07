from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.response import Response

from .models import *
from .serializers import SnippetSerializer
from django.shortcuts import get_object_or_404


class SnippetList(APIView):
    def get(self, request):
        snippet = Snippet.objects.all()
        ser_data = SnippetSerializer(instance=snippet, many=True)
        return Response(data=ser_data.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        ser_data = SnippetSerializer(data=data)
        if ser_data.is_valid():
            ser_data.save()
            return Response(data=ser_data.data, status=status.HTTP_201_CREATED)
        return Response(data=ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class SnippetDetail(APIView):

    def get(self, request, pk):
        snippet = get_object_or_404(Snippet, pk=pk)
        ser_data = SnippetSerializer(instance=snippet)
        return Response(ser_data.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        snippet = get_object_or_404(Snippet, pk=pk)
        data = request.data
        ser_data = SnippetSerializer(instance=snippet, data=data, partial=True)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        snippet = get_object_or_404(Snippet, pk=pk)
        snippet.delete()
        return Response({"message": "snippet was deleted"})


