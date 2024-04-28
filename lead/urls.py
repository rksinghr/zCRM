from django.urls import path
from . import views

urlpatterns = [
    path('leads_list/', views.leads_list, name='leads_list'),
    path('view_lead/<int:pk>', views.view_lead, name='view_lead'),
    path('delete_lead/<int:pk>', views.delete_lead, name='delete_lead'),
    path('add_lead/', views.add_lead, name='add_lead'),
    path('update_lead/<int:pk>', views.update_lead, name='update_lead'),
]