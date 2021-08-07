from django.urls import path
from . import views


app_name = "college"
urlpatterns = [
    path('home/', views.home, name='home'),
    path('student_application/', views.student_application, name='student_application'),
    path('applying/', views.applying, name='applying'),
    path('stu_register/',views.stu_register,name='stu_register'),
    path('stu_login/',views.stu_login,name='stu_login'),
    path('stu_details/',views.stu_details,name='stu_details'),
    path('student_list/',views.student_list,name='student_list'),
    path('stu_logout/',views.stu_logout,name='stu_logout'),
    path('staff_register/',views.staff_register,name='staff_register'),
    path('staff_login/',views.staff_login,name='staff_login'),
    path('staff_details/',views.staff_details,name='staff_details'),
    path('staff_logout/',views.staff_logout,name='staff_logout'),
    path('staff_list/',views.staff_list,name='staff_list'),
]