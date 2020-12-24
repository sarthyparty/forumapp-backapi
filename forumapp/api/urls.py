from django.conf.urls import url
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import *

urlpatterns = [
    url(r'^questions/$', QuestionCreateView.as_view(), name='questions'),
    url(r'^questions/(?P<pk>[0-9]+)$', QuestionDetailView.as_view(), name='question_detail'),
    url(r'^answers/$', AnswerCreateView.as_view(), name='answers'),
    url(r'^answers/(?P<pk>[0-9]+)$', AnswerDetailView.as_view(), name='answer_detail'),
    url(r'^questions/recent$', RecentView.as_view(), name='recent_questions'),
    url(r'^questions/unanswered$', UnansweredView.as_view(), name='unanswered_question_view'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]