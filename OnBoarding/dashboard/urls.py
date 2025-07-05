from django.urls import path
from .views import DashboardView, LogoutViaGet, login_view, set_language

urlpatterns = [
    path("", DashboardView.as_view(), name="dashboard"),
    path("login/", login_view, name="login"),
    path("logout/", LogoutViaGet.as_view(), name="logout"),
    path("set-language/<str:language_code>/", set_language, name="set_language"),
]
