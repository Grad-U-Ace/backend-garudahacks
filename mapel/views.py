from rest_framework import viewsets
from .models import Mapel, Topic, Activity, Modul, Exercise, Soal
from .serializers import MapelSerializer, TopicSerializer, ActivitySerializer, ModulSerializer, ExerciseSerializer, SoalSerializer

class MapelViewSet(viewsets.ModelViewSet):
    queryset = Mapel.objects.all()
    serializer_class = MapelSerializer

class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            obj = self.get_object()
            if obj.type == 'modul':
                return ModulSerializer
            elif obj.type == 'exercise':
                return ExerciseSerializer
        return self.serializer_class

class ModulViewSet(viewsets.ModelViewSet):
    queryset = Modul.objects.all()
    serializer_class = ModulSerializer

class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

class SoalViewSet(viewsets.ModelViewSet):
    queryset = Soal.objects.all()
    serializer_class = SoalSerializer