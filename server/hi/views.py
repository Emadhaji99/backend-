from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("hello world")
def about(request):
    return HttpResponse("say this is")
# Create your views here.
