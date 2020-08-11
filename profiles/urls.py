from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('edit/<username>', views.edit_profile, name='edit_profile'),
    path('update/<username>', views.update_profile, name='update_profile'),
    path('user_books/<username>', views.user_books, name='user_books'),
    path('ask_book/<int:book_id>/', views.ask_book, name='ask_book'),
    path('rmv_book/<int:book_id>/', views.rmv_book, name='rmv_book'),
]
