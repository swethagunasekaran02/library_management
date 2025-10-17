from django.urls import path
from . import views

app_name = 'customer'

urlpatterns = [
    path('', views.member_list, name='member_list'),
    path('<int:pk>/', views.member_detail, name='member_detail'),
    path('add/', views.add_member, name='add_member'),
    path('<int:pk>/edit/', views.edit_member, name='edit_member'),
]
