from django.urls import path, re_path, include
from . import views

app_name = 'blogs'

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/<int:blog_id>', views.blog, name='blog'),
    path('blog/new_blog', views.new_blog, name='new_blog'),
    path('blog/edit_blog/<int:blog_id>', views.edit_blog, name='edit_blog'),
]
