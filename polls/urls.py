 # polls/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),      # http://127.0.0.1:8000/polls/
    path("hello/", views.hello, name="hello") # http://127.0.0.1:8000/polls/hello/
]
