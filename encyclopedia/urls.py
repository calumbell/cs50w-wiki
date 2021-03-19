from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("edit",  views.edit, name="edit"),
    path("random", views.random, name="random"),
    path("search", views.search, name="search"),
    path("wiki/<str:name>", views.entry, name="entry"),
    path("create", views.create, name="create"),
]
