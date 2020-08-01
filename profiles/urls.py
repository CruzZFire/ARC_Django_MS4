from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('reviews/<profile_id>', views.user_reviews, name='user_reviews'),
]
