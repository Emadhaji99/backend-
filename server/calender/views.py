from django.shortcuts import render
from datetime import datetime
date=datetime.now()
def founder(request):
    if date.day()==1 and date.month()==1:
        return render()

# Create your views here.
