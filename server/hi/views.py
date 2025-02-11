from django.shortcuts import render
from django.http import HttpResponse
def index(request,name):
    return HttpResponse(f"hello {name}")
def about(request):
    return HttpResponse("say this is about the django")
# Create your views here.
