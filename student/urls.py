from django.urls import path 
from . import views

urlpatterns = [
    path('', views.listStudent,name='listStudent'),
    path('student/<int:pk>', views.getStudent, name='getStudent'),
    path('student/add', views.addStudent, name='addstudent'),
    path('student/delete/<int:pk>', views.deleteStudent, name= 'deleteStudent')
]
