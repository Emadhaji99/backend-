from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request,"hi\\index.html",)
def greet(request,tag):
    context={
        "name":tag,
        "my_list":["banana","orange"],
    }
    return render(request,"hi\\greet.html",context)