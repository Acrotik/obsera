from django.contrib import admin
from django.urls import path, include
from website.views import index, success, deny

urlpatterns = [
    path('admin/', admin.site.urls),
    path('defaultsite/', index, name='index'),
    path('', index, name='index'),  # root URL serves index.html
    path('dashboard/', include('dashboard.urls')),  # dashboard now at /dashboard/
    path('i18n/', include('django.conf.urls.i18n')),
    path('success/', success, name='success'),  # Success page
    path('deny/', deny, name='deny'),  # Deny page
]
