from django.urls import path
from . import views

urlpatterns = [
    path('bcrecord_list/', views.list_records, name='bcrecord_list'),
    path('bcrecord/<int:pk>', views.view_record, name='bcrecord'),
    path('bcdelete_record/<int:pk>', views.delete_record, name='bcdelete_record'),
    path('bcadd_record/', views.add_record, name='bcadd_record'),
    path('bcupdate_record/<int:pk>', views.update_record, name='bcupdate_record'),
]