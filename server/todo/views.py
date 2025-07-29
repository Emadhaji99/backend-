from django.shortcuts import render
from django.http import HttpResponse
from .forms import content
#-------------------------
def task(request):
    context={"tas":["one","two","three","four"],}
    return render(request,"todo\\tasks.html",context)
#-------------------------
def add(request):
    context={"ta":[1,2,34],"Form":content()}
    return render(request,"todo\\add.html",context)
#-------------------------
def submit(request):
    if request.method=="POST":
        return HttpResponse("the form completed and the method is post")
    else:
        return HttpResponse("this is get method ")
