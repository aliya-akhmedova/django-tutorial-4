# polls/views.py
from django.http import HttpResponse
from django.shortcuts import render

# Sadə test view (ilk səhifə)
def index(request):
    return HttpResponse("Salam! Bu 'polls' app-indəki ana səhifədir ")

# Template istifadə edən view
def hello(request):
    context = {"name": "Aliya"}  # HTML-ə göndərəcəyimiz məlumat
    return render(request, "polls/hello.html", context)
