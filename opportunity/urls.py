from django.urls import path
from . import views

urlpatterns = [
    path('opportunity_list/', views.opportunity_list, name='opportunity_list'),
    path('view_opportunity/<int:pk>', views.view_opportunity, name='view_opportunity'),
    path('delete_opportunity/<int:pk>', views.delete_opportunity, name='delete_opportunity'),
    path('add_opportunity/', views.add_opportunity, name='add_opportunity'),
    path('update_opportunity/<int:pk>', views.update_opportunity, name='update_opportunity'),
]