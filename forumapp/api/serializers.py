from rest_framework.serializers import ModelSerializer

from .models import Question


class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = ('pk', 'content', 'time')
        extra_kwargs = {
            'id': {'read_only': True}
        }
