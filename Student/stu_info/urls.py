from django.urls import path
from .views import ( add_stu,show_stu,update_stu,delete_stu )

urlpatterns = [
    path('add/',add_stu,name='add_student'),
    path('show/',show_stu,name='show_student'),
    path('update/<int:pk>/',update_stu,name='update_student'),
    path('delete/<int:pk>/',delete_stu,name='delete_student')
]