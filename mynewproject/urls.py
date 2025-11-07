# mynewproject/urls.py
from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponse

def home(request):
    return HttpResponse("Django layihəmə xoş gəlmisən ")

urlpatterns = [
    path("", home),  # əsas səhifə
    path("polls/", include("polls.urls")),  # polls app buradan çağırılır
    path("admin/", admin.site.urls),
]
