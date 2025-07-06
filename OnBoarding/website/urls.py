from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.i18n import set_language
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('success/', views.success, name='success'),
    path('deny/', views.deny, name='deny'),
    path('set-language/', set_language, name='set_language'),
]
