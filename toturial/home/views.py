from django.http import HttpResponse
from rest_framework import status, generics
from rest_framework.decorators import APIView
from rest_framework.response import Response

from .models import *
from .serializers import AlbumSerializer
from django.shortcuts import get_object_or_404


# class AlbumList(APIView):
#     def get(self, request):
#         albums = Album.objects.all()
#         ser_data = AlbumSerializer(instance=albums, many=True)
#         return Response(data=ser_data.data, status=status.HTTP_200_OK)
#
#     def post(self, request):
#         data = request.data
#         ser_data = AlbumSerializer(data=data)
#         if ser_data.is_valid():
#             ser_data.save()
#             return Response(data=ser_data.data, status=status.HTTP_201_CREATED)
#         return Response(data=ser_data.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class AlbumDetail(APIView):
#     def get(self, request, pk):
#         album = get_object_or_404(Album, pk=pk)
#         ser_data = AlbumSerializer(instance=album)
#         return Response(data=ser_data.data, status=status.HTTP_200_OK)
#
#     def put(self, request, pk):
#         album = get_object_or_404(Album, pk=pk)
#         data = request.data
#         ser_data = AlbumSerializer(instance=album, data=data)
#         if ser_data.is_valid():
#             ser_data.save()
#             return Response(data=ser_data.data, status=status.HTTP_201_CREATED)
#         return Response(data=ser_data.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         album = get_object_or_404(Album, pk=pk)
#         album.delete()
#         return Response({"message": "album was deleted"}, status=status.HTTP_204_NO_CONTENT)


class AlbumList(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class AlbumDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
