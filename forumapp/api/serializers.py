from rest_framework.serializers import ModelSerializer

from .models import Question


class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = ('pk', 'content', 'time_asked', 'email', 'has_answer')
        extra_kwargs = {
            'id': {'read_only': True}
        }

class AnswerSerializer(ModelSerializer):
    class Meta:
        model = Answer
        fields = ('pk', 'content', 'time_asked', 'email', 'question')
        extra_kwargs = {
            'id': {'read_only': True}
        }
