from django.urls import path
from . import views

urlpatterns = [
    path('crecord_list/', views.list_records, name='crecord_list'),
    path('crecord/<int:pk>', views.view_record, name='crecord'),
    path('cdelete_record/<int:pk>', views.delete_record, name='cdelete_record'),
    path('cadd_record/', views.add_record, name='cadd_record'),
    path('cupdate_record/<int:pk>', views.update_record, name='cupdate_record'),
]