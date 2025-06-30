from django.shortcuts import render
def task(request):
    context={"tas":["one","two","three","four"],}
    return render(request,"todo\\tasks.html",context )

def add(request):
    context={"ta":[1,2,34]}
    return render(request,"todo\\add.html",context)

