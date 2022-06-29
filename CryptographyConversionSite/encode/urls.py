from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('encode/base64/', views.Base64),
    path('encode/MD5/', views.MD5),
    path('encode/SHA1/',views.SHA1),
    path('encode/SHA224/', views.SHA224),
    path('encode/SHA256/', views.SHA256),
    path('encode/SHA384/', views.SHA384),
    path('encode/SHA512/', views.SHA512),
]
