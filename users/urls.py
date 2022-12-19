from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('get_users/', views.get_users),
    path('get_user_by_id/<str:id>', views.get_user_by_id),
    path('add_user/', views.add_user),
    path('update_user/', views.update_user),
    path('delete_user/<id>', views.delete_user),
]
