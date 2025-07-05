from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Form page
    path('success/', views.success, name='success'),  # Success page
    path('deny/', views.deny, name='deny'),  # Deny page
]
