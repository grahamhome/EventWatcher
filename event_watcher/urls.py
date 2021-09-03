from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("schema/new", views.create_schema, name="create schema")
]