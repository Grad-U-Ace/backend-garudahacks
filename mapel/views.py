import openai
from django.db import transaction
from openai import OpenAI
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

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


class ModulViewSet(viewsets.ModelViewSet):
    serializer_class = ModulSerializer

    def get_queryset(self):
        return Modul.objects.filter(topic_id=self.kwargs['topic_pk'])

    @transaction.atomic
    def perform_create(self, serializer):
        topic_id = self.kwargs['topic_pk']
        modul = Modul(
            title=serializer.validated_data['title'],
            file=serializer.validated_data['file'],
            topic_id=topic_id
        )
        modul.save()
        serializer.instance = modul

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


def generate_questions(topic, title, description, num_questions=5):
    prompt = f"Generate {num_questions} questions for an exercise. Topic: {topic}. Exercise title: {title}. Exercise description: {description}. Format each question-answer pair as 'Q: [question] A: [answer]' in a single string."

    try:
        client = OpenAI()
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that generates educational questions."},
                {"role": "user", "content": prompt}
            ]
        )

        # Parse the response and convert it to a list of dictionaries
        return response.choices[0].message.content.strip().split('\n')
    except Exception as e:
        print(f"Error generating questions: {e}")
        return None


class ExerciseViewSet(viewsets.ModelViewSet):
    serializer_class = ExerciseSerializer

    def get_queryset(self):
        return Exercise.objects.filter(topic_id=self.kwargs['topic_pk'])

    @transaction.atomic
    def perform_create(self, serializer):
        topic_id = self.kwargs['topic_pk']
        exercise = Exercise(
            title=serializer.validated_data['title'],
            description=serializer.validated_data['description'],
            topic_id=topic_id
        )
        exercise.save()
        serializer.instance = exercise

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=True, methods=['post'])
    def generate_questions(self, request, mapel_pk=None, topic_pk=None, pk=None):
        exercise = self.get_object()
        topic = exercise.topic.name
        num_questions = request.data.get('num_questions', 5)

        generated_questions = generate_questions(topic, exercise.title, exercise.description, num_questions)

        if not generated_questions:
            return Response({"error": "Failed to generate questions"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        print(generated_questions)
        created_soal = []
        for q_and_a in generated_questions:
            question, answer = q_and_a.split('A:')
            question = question.replace('Q:', '').strip()
            answer = answer.strip()
            soal = Soal.objects.create(
                question=question,
                answer=answer,
                exercise=exercise
            )
            created_soal.append(SoalSerializer(soal).data)

        return Response(created_soal, status=status.HTTP_201_CREATED)

class SoalViewSet(viewsets.ModelViewSet):
    serializer_class = SoalSerializer

    def get_queryset(self):
        return Soal.objects.filter(exercise_id=self.kwargs['exercise_pk'])