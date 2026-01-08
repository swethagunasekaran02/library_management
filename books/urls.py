# books/urls.py

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'books' 

urlpatterns = [
    path('', views.home, name='home'),
    path('books', views.book_list, name='book_list'),
    path('create/', views.book_create, name='book_create'),
    path('<int:pk>/', views.book_detail, name='book_detail'),
    path('<int:pk>/edit/', views.book_edit, name='book_edit'),
    path('delete/<int:pk>/', views.book_delete, name='book_delete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

