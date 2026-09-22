from django.urls import path
from . import views

urlpatterns=[

path('', views.home),
path('dashboard/', views.dashboard),

path(
'students/',
views.student_list
),

path(
'add/',
views.add_student
),
path(
    'delete/<int:id>',
    views.delete_student
),
path(
    'update/<int:id>',
    views.update_student
),
path(
    'class/<str:class_name>',
    views.class_students
),
path(
'class-list/',
views.class_list
),
]