from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # admin is present but you won't use it for this assignment
    path('', include('inventory.urls')),
]
