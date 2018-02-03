from django.urls import include, path, re_path

from . import views

app_name = 'learning_logs'

urlpatterns = [
    # Home page
    re_path(r'^$', views.index, name='index')
]
