from django.shortcuts import render
from datetime import datetime
def d(request):
    date=datetime.now()
    day=date.day
    month=date.month
    context={
    "newyear":month==1 and day==1
    }
    return render(request,"calender\\calender.html",context)


# Create your views here.

