from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('invoice/create_project/', views.create_project, name='create_project'),
    path('invoice/save_boq/', views.save_boq, name='save_boq'),
    path('invoice/<int:project_id>/boq/', views.create_BOQ, name='create_BOQ'),
    path('invoice/<int:invoice_id>/pdf/', views.generate_invoice_pdf, name='generate_invoice_pdf'),
]
