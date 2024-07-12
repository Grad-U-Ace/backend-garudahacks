from rest_framework import serializers

from activity.models import Activity, Exercise, Module, Soal


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'


class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = '__all__'


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'

class SoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Soal
        fields = '__all__'