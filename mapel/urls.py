from django.urls import path
from django.urls.conf import include
from rest_framework_nested import routers

from mapel.views import MapelViewSet, TopicViewSet

router = routers.SimpleRouter()
router.register(r'mapels', MapelViewSet, basename='mapels')

mapel_router = routers.NestedSimpleRouter(router, r'mapels', lookup='mapel')
mapel_router.register(r'topics', TopicViewSet, basename='topics')


urlpatterns = [
    path(r'', include(router.urls)),
    path(r'', include(mapel_router.urls)),
]
