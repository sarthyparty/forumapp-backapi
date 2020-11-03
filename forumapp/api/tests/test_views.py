# movies-api/movies/api/tests/test_views.py
from datetime import datetime

from django.shortcuts import reverse

from rest_framework.test import APITestCase

from ..models import Question


class TestNoteApi(APITestCase):
    def setUp(self):
        # create movie
        self.question = Question(content="What time is it?", time=datetime.now())
        self.question.save()

    def test_question_creation(self):
        response = self.client.post(reverse('questions'), {
            'content': 'What is tastiest milkshake?',
            'time': datetime.now()
        })

        # assert new movie was added
        self.assertEqual(Question.objects.count(), 2)

        # assert a created status code was returned
        self.assertEqual(201, response.status_code)

    def test_getting_questions(self):
        response = self.client.get(reverse('questions'), format="json")
        self.assertEqual(len(response.data), 1)

    def test_updating_question(self):
        response = self.client.put(reverse('detail', kwargs={'pk': 1}), {
            'content': 'What time is it? updated',
            'time': datetime.now()
        }, format="json")

        # check info returned has the update
        self.assertEqual('What time is it? updated', response.data['content'])

    def test_deleting_question(self):
        response = self.client.delete(reverse('detail', kwargs={'pk': 1}))

        self.assertEqual(204, response.status_code)
