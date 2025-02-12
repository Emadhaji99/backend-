from django.shortcuts import render
from django.http import HttpResponse
def index(request,name):
    return HttpResponse(f"hello {name}")
def about(request):
    return HttpResponse("<h1>say this is about the django</h1>")
# Create your views here.
