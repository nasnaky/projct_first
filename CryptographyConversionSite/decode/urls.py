from django.urls import path

from . import views

urlpatterns = [
    path('base64/', views.Base64)
]
