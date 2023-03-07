from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Snippet
from .serializers import SnippetSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404


@csrf_exempt
def snippet_list(request):
    if request.method == "GET":
        snippets = Snippet.objects.all()
        ser_data = SnippetSerializer(instance=snippets, many=True)
        return JsonResponse(ser_data.data, safe=False)
    elif request.method == "POST":
        data = request.data
        ser_data = SnippetSerializer(data=data)
        if ser_data.is_valid():
            ser_data.save()
            return JsonResponse(ser_data.data, status=status.HTTP_201_CREATED)
        return JsonResponse(ser_data.data, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def snippet_detail(request, pk):
    if request.method == "GET":
        snippet = get_object_or_404(Snippet, pk=pk)
        ser_data = SnippetSerializer(instance=snippet)
        return JsonResponse(ser_data.data, status=status.HTTP_200_OK)

    elif request.method == "PUT":
        snippet = get_object_or_404(Snippet, pk=pk)
        data = request.data
        ser_data = SnippetSerializer(instance=snippet, data=data, partial=True)
        if ser_data.is_valid():
            ser_data.save()
            return JsonResponse(ser_data.data, status=status.HTTP_201_CREATED)
        return JsonResponse(ser_data.data, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        snippet = get_object_or_404(Snippet, pk=pk)
        snippet.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)