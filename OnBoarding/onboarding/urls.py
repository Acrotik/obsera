from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include
from django.contrib import admin
from website.views import index, success, deny

urlpatterns = [
    # any patterns you want *outside* the language prefix go here
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('success/', success, name='success'),
    path('deny/', deny, name='deny'),

]

urlpatterns += i18n_patterns(
    path('', include('website.urls')),
)
