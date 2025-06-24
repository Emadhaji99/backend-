from django.shortcuts import render
def task(request):
    context={"task":["one","two","three","four"],}
    return render(request,"todo\\tasks.html",context )

def add(request):
    return render(request,"todo\\add.html")

