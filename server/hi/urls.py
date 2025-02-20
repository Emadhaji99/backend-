from django.urls import path
import sys
sys.path.append("C:\\Users\\Sara Tel\\backend-\\server\\hi")
import views
urlpatterns=[
    path('ad/',views.index,name="index"),
    path('<str:tag>/',views.greet,name="greet")
]