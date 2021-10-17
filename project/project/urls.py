"""project URL Configuration
"""
from django.urls import path, include

urlpatterns = [
    path('', include('contacts.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
