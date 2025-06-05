from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("fuck you ")
def greet(request,tag):
    context={
        "name":tag,
        "my_list":["banana","orange"],
    }
    return render(request,"hi\\greet.html",context)