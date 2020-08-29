from rest_framework import serializers
from tutorials.models import Tutorial
from tutorials.models import TutorialDemoModelPersonalDetails


class TutorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutorial
        fields = ('id',
                  'title',
                  'description',
                  'published')


class TutorialDemoModelPersonalDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TutorialDemoModelPersonalDetails
        fields = ('id',
                  'Name',
                  'Address',
                  'Age')