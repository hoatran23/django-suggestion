from rest_framework import serializers
from .models import *

class CombinationdataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Combinationdata
        fields = ('__all__')


class PollsQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PollsQuestion
        fields = ('__all__')