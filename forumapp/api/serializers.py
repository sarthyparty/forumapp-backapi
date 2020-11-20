from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField

from .models import Question, Answer


class QuestionSerializer(ModelSerializer):
    answers = PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Question
        fields = ('pk', 'content', 'email', 'created_at', 'has_answer', 'answers')
        extra_kwargs = {
            'id': {'read_only': True}
        }

class AnswerSerializer(ModelSerializer):
    class Meta:
        model = Answer
        fields = ('pk', 'content', 'created_at', 'email', 'question')
        extra_kwargs = {
            'id': {'read_only': True}
        }
