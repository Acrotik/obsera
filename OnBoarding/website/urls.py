from django.conf.urls.i18n import i18n_patterns
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Form page
    path('success/', views.success, name='success'),  # Success page
    path('deny/', views.deny, name='deny'),  # Deny page
]


urlpatterns += i18n_patterns(
    path('set_language/', views.set_language, name='set_language'),  # Language switching URL
)