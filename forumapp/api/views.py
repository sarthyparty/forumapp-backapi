from django.shortcuts import render
import datetime

# Create your views here.
from rest_framework import filters
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from .models import *
from .serializers import QuestionSerializer, AnswerSerializer


class DynamicSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])
        
class QuestionCreateView(ListCreateAPIView):
    filter_backends = (DynamicSearchFilter,)
    permission_classes = (IsAuthenticated,)
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerCreateView(ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class AnswerDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class UnansweredView(ListCreateAPIView):
    queryset = Question.objects.filter(has_answer=False).order_by('-created_at')[0:10]
    serializer_class = QuestionSerializer


class RecentView(ListCreateAPIView):
    queryset = Question.objects.order_by('-created_at')[0:10]
    serializer_class = QuestionSerializer
