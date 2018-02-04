from django.urls import include, path, re_path

from . import views

app_name = 'learning_logs'

urlpatterns = [
    # Home page
    re_path(r'^$', views.index, name='index'),
    # Show all the topics
    re_path(r'^topics/$', views.topics, name='topics'),
    # Specific topic
    re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    # New topic
    re_path(r'^new_topic/$', views.new_topic, name='new_topic'),
    # New entry
    re_path(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry,
            name='new_entry'),
    # Edit entry
    re_path(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry,
            name='edit_entry'),
]
