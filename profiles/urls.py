from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('ask_book/<int:book_id>/', views.ask_book, name='ask_book'),
]
