from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_books, name='all_books'),
    path('search/', views.search_books, name='search_books'),
    path('<int:book_id>/', views.book_detail, name='book_detail'),
    path('set_promoted/<int:book_id>/', views.set_promoted, name='set_promoted'),
]
