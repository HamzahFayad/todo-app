from django.urls import path
from . import views

urlpatterns = [
    path('show/', views.task_list, name='task-list'),
    path('show/<int:pk>/', views.TaskDetailsView.as_view(), name='task-details'),
    path('add/', views.TaskCreateView.as_view(), name='task-create'),
    path('show/edit/<int:pkc>/', views.TaskUpdateView.as_view(), name="edit-task"),
    path('show/delete/<int:pkc>/', views.task_delete, name='task-delete'),
]