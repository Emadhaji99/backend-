from django.urls import path
from . import views
app_name="todo"
urlpatterns=[
    path('task/',views.task,name="task"),
    path('add/',views.add,name="add"),
    path('submit/',views.submit,name="submit")
]