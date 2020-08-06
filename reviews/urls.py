from django.urls import path
from . import views

urlpatterns = [
    path('<int:book_id>/', views.book_reviews, name='book_reviews'),
    path('<username>/', views.user_reviews, name='user_reviews'),
]
