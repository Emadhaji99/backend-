from django.urls import path
from . import views
urlpatterns=[
    path('ad/',views.index,name="index"),
    path('<str:tag>/',views.greet,name="greet")
]