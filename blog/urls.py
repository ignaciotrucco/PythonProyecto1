from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path("post/list", views.post_list, name="post_list"),
    path("post/create", views.post_create, name="post_create"),
]