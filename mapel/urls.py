from django.urls import path, include
from rest_framework_nested import routers
from .views import MapelViewSet, TopicViewSet, ActivityViewSet, ModulViewSet, ExerciseViewSet, SoalViewSet

router = routers.DefaultRouter()
router.register(r'mapel', MapelViewSet)

mapel_router = routers.NestedDefaultRouter(router, r'mapel', lookup='mapel')
mapel_router.register(r'topics', TopicViewSet, basename='mapel-topics')

topic_router = routers.NestedDefaultRouter(mapel_router, r'topics', lookup='topic')
topic_router.register(r'activities', ActivityViewSet, basename='topic-activities')

exercise_router = routers.NestedDefaultRouter(topic_router, r'activities', lookup='activity')
exercise_router.register(r'soal', SoalViewSet, basename='exercise-soal')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(mapel_router.urls)),
    path('', include(topic_router.urls)),
    path('', include(exercise_router.urls)),
]