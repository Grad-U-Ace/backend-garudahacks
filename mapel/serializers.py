from django.db import transaction
from rest_framework import serializers
from .models import Mapel, Topic, Activity, Modul, Exercise, Soal


class SoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Soal
        fields = ['id', 'question', 'answer', 'used']


class ModulSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modul
        fields = ['id', 'title', 'file', 'type', 'topic']
        read_only_fields = ['type']


class ExerciseSerializer(serializers.ModelSerializer):
    soal_set = SoalSerializer(many=True, read_only=True)

    class Meta:
        model = Exercise
        fields = ['id', 'title', 'description', 'type', 'topic', 'soal_set']
        read_only_fields = ['type']


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['id', 'title', 'type']


class TopicSerializer(serializers.ModelSerializer):
    activities = ActivitySerializer(many=True, read_only=True)

    class Meta:
        model = Topic
        fields = ['id', 'name', 'mapel', 'activities', 'start_date', 'end_date']


class MapelSerializer(serializers.ModelSerializer):
    topic_set = TopicSerializer(many=True, read_only=True)

    class Meta:
        model = Mapel
        fields = ['id', 'name', 'topic_set']