from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('record_list/<int:key>', views.list_records, name='record_list'),
    path('record/<int:key>/<int:pk>', views.view_record, name='record'),
    path('delete_record/<int:key>/<int:pk>', views.delete_record, name='delete_record'),
    path('add_record/<int:key>', views.add_record, name='add_record'),
    path('update_record/<int:key>/<int:pk>', views.update_record, name='update_record'),
]
