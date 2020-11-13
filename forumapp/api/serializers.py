from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField

from .models import Question, Answer


class QuestionSerializer(ModelSerializer):
    answers = PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Question
        fields = ('pk', 'content', 'time_asked', 'email', 'has_answer', 'answers')
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
