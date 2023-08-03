from .models import Pass, Image, Coord, User, Level
from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'surname', 'last_name', 'email', 'phone']


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ['winter', 'summer', 'autumn', 'spring']


class CoordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coord
        fields = ['latitude', 'longitude', 'height']


class ImageSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Image
        fields = ['id', 'data', 'title']


class PassSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    user = UsersSerializer()
    coords = CoordSerializer()
    level = LevelSerializer()
    images = ImageSerializer(many=True)

    class Meta:
        model = Pass
        fields = ['id', 'user', 'coords', 'level', 'status', 'beauty_title', 'title', 'other_titles', 'connect',
                  'add_time', 'images']
