from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response

from mapel.models import Mapel, Topic
from mapel.serializers import MapelSerializer, TopicSerializer


# Create your views here.
class MapelViewSet(viewsets.ViewSet):
    serializer_class = MapelSerializer

    def list(self, request,):
        queryset = Mapel.objects.filter()
        serializer = MapelSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Mapel.objects.filter()
        client = get_object_or_404(queryset, pk=pk)
        serializer = MapelSerializer(client)
        return Response(serializer.data)

    def create(self, request):
        serializer = MapelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, pk=None):
        queryset = Mapel.objects.filter(pk=pk)
        mapel = get_object_or_404(queryset, pk=pk)
        mapel.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TopicViewSet(viewsets.ViewSet):
    serializer_class = TopicSerializer

    def list(self, request, mapel_pk=None):
        queryset = Topic.objects.filter(mapel=mapel_pk)
        serializer = TopicSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, mapel_pk=None):
        queryset = Topic.objects.filter(pk=pk, mapel=mapel_pk)
        topic = get_object_or_404(queryset, pk=pk)
        serializer = TopicSerializer(topic)
        return Response(serializer.data)

    def create(self, request, mapel_pk=None):
        serializer = TopicSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, pk=None, mapel_pk=None):
        queryset = Topic.objects.filter(pk=pk, mapel=mapel_pk)
        topic = get_object_or_404(queryset, pk=pk)
        topic.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)