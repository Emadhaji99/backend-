from django.urls import path
import sys
sys.path.append("C:\\Users\\Sara Tel\\backend-\\server\\hi")
import views
urlpatterns=[
    path('<str:name>/',views.index,name="hello user"),
    path("about/",views.about,name="about page"),
]