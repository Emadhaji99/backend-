from django.shortcuts import render
from django.urls import reverse
def task(request):
    context={"tas":["one","two","three","four"],}
    return render(request,"todo\\tasks.html",context )

def add(request):
    context={"ta":[1,2,34]}
    return render(request,"todo\\add.html",context)

