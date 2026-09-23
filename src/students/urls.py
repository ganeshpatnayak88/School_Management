from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('robots.txt', views.robots_txt, name='robots_txt'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('students/', views.student_list, name='student_list'),
    path('add/', views.add_student, name='add_student'),
    path('delete/<int:id>', views.delete_student, name='delete_student'),
    path('update/<int:id>', views.update_student, name='update_student'),
    path('class/<str:class_name>', views.class_students, name='class_students'),
    path('class-list/', views.class_list, name='class_list'),
    path(
    'google3ba06830d3fd2c2f.html',
    views.google_verification,
    name='google_verification'
),
]