from django.contrib import admin
from django.urls import include, path

from todos import views

# dev_1
urlpatterns = [
    path("", views.todo_list, name="todo_list"),
    path("post/", views.todo_post, name="todo_post"),#dev3
]
