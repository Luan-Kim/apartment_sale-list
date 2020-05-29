from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('new_apt_list', views.new_apt_list, name='new_apt_list')
]