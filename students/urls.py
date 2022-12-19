from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('get_students/', views.get_students),
    path('get_student_by_id/<str:id>', views.get_student_by_id),
    path('get_students_by_name/<str:name>', views.get_students_by_name),
    path('add_student/', views.add_student),
    path('update_student/', views.update_student),
    path('delete_student/<id>', views.delete_student),
]
