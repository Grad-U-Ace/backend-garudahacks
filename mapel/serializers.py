from rest_framework import serializers

from mapel.models import Mapel, Topic


class MapelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mapel
        fields = '__all__'

class TopicSerializer(serializers.ModelSerializer):
    parent_lookup_kwargs = {
        'mapel_pk': 'mapel__pk',
    }

    class Meta:
        model = Topic
        fields = '__all__'