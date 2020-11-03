# forumapp-backapi/forumapp/api/tests/test_models.py

from django.test import TestCase

from ..models import Question

from datetime import datetime


class TestQuestionModel(TestCase):
    def setUp(self):
        self.question = Question(content="How long was the 30 years war?", time=datetime.now())
        self.question.save()

    def test_question_creation(self):
        self.assertEqual(Question.objects.count(), 1)

    def test_question_representation(self):
        self.assertEqual(self.question.content, str(self.question))