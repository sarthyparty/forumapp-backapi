from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^questions/$', QuestionCreateView.as_view(), name='questions'),
    url(r'^questions/(?P<pk>[0-9]+)$', QuestionDetailView.as_view(), name='question_detail'),
    url(r'^answers/$', AnswerCreateView.as_view(), name='answers'),
    url(r'^answers/(?P<pk>[0-9]+)$', AnswerDetailView.as_view(), name='answer_detail'),
]