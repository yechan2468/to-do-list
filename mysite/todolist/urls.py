from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='task_list'),
    path('<int:task_id>/', views.detail, name='task_detail'),
    path('task/create/', views.task_create, name='task_create'),
    path('task/edit/<int:task_id>', views.task_edit, name='task_edit'),
    path('task/delete/<int:task_id>/', views.task_delete, name='task_delete'),
]
