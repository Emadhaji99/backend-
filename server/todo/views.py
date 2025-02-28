from django.shortcuts import render

context={"task":["one","two","three","four"]}
def task(request):
    return render(request,"todo\\todo.html",context )

