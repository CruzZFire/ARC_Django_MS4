from django.urls import path
from . import views

urlpatterns = [
    path('<int:book_id>/', views.book_reviews, name='book_reviews'),
    path('<username>/', views.user_reviews, name='user_reviews'),
    path('edit/<int:review_id>/', views.edit_review, name='edit_review'),
    path('del/<int:review_id>/', views.delete_review, name='delete_review'),
]
