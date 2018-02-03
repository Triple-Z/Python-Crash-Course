from django.urls import include, path, re_path

from . import views

app_name = 'learning_logs'

urlpatterns = [
    # Home page
    re_path(r'^$', views.index, name='index'),
    # Show all the topics
    re_path(r'^topics/$', views.topics, name='topics'),
    # Specific topic
    re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic')
]
