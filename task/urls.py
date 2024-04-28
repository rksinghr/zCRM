from django.urls import path
from . import views

urlpatterns = [
    path('task_list/', views.task_list, name='task_list'),
    path('view_task/<int:pk>', views.view_task, name='view_task'),
    path('delete_task/<int:pk>', views.delete_task, name='delete_task'),
    path('add_task/', views.add_task, name='add_task'),
    path('update_task/<int:pk>', views.update_task, name='update_task'),
]