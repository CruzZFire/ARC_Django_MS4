"""arc_community URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('books.urls')),
    path('/', include('home.urls')),
    path('profiles/', include('profiles.urls')),
    path('subcritions/', include('subcritions.urls')),
]
