from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Here I will build a railway booking system!")

def hello(request):
   text = """<h1>welcome to my app !</h1>"""
   return HttpResponse(text)
