from django.shortcuts import render
def index(request):
    return render(request,"hi/index.html") 
def greet(request,tag):
    context={
        "name":tag,
        "list":["banana","orange"],
    }
    return render(request,"hi\greet.html",context)