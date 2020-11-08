from django.conf.urls import url

from .views import QuestionCreateView, QuestionDetailView

urlpatterns = [
    url(r'^questions/$', QuestionCreateView.as_view(), name='questions'),
    url(r'^questions/(?P<pk>[0-9]+)$', QuestionDetailView.as_view(), name='detail'),
]