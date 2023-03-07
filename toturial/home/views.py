from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from .serializers import SnippetSerializer
from django.shortcuts import get_object_or_404


@api_view(["GET", "POST"])
def snippet_list(request):
    if request.method == "GET":
        snippet = Snippet.objects.all()
        ser_data = SnippetSerializer(instance=snippet, many=True)
        return Response(data=ser_data.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        data = request.data
        ser_data = SnippetSerializer(data=data)
        if ser_data.is_valid():
            ser_data.save()
            return Response(data=ser_data.data, status=status.HTTP_201_CREATED)
        return Response(data=ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def snippet_detail(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    if request.method == "GET":
        ser_data = SnippetSerializer(instance=snippet)
        return Response(ser_data.data, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        data = request.data
        ser_data = SnippetSerializer(instance=snippet, data=data, partial=True)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        snippet.delete()
        return Response({"message": "snippet was deleted"})
