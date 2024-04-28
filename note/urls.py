from django.urls import path
from . import views

urlpatterns = [
    path('note_list/', views.note_list, name='note_list'),
    path('view_note/<int:pk>', views.view_note, name='view_note'),
    path('delete_note/<int:pk>', views.delete_note, name='delete_note'),
    path('add_note/', views.add_note, name='add_note'),
    path('update_note/<int:pk>', views.update_note, name='update_note'),
]