from django.urls import path
from . import views

urlpatterns = [
    path("schema/new", views.create_schema, name="create schema"),
    path("event/new", views.create_events, name="create event")
]