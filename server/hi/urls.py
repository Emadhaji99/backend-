from django.urls import path
import sys
sys.path.append("C:\\Users\\Sara Tel\\backend-\\server\\hi")
import views
urlpatterns=[
    path('ad/',views.index,name="greeting")
]