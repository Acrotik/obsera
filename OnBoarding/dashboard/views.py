from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import EmailAuthenticationForm
from django.utils.translation import activate
from django.http import HttpResponseRedirect
from django.conf import settings


class LogoutViaGet(LogoutView):
    next_page = reverse_lazy("login")
    http_method_names = ["get", "post"]

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class DashboardView(LoginRequiredMixin, TemplateView):
    login_url = "/login/"
    template_name = "base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Determine user role
        if self.request.user.is_staff:
            user_role = "Admin"
        elif self.request.user.groups.filter(name="Manager").exists():
            user_role = "Manager"
        else:
            user_role = "User"

        # Add user_role to context
        context["user_role"] = user_role
        return context


def login_view(request):
    if request.method == "POST":
        form = EmailAuthenticationForm(data=request.POST)

        if form.is_valid():
            login(request, form.user_cache)
            return redirect("dashboard")
        else:
            return render(request, "login.html", {"form": form})
    else:
        form = EmailAuthenticationForm()

    return render(request, "login.html", {"form": form})


LANGUAGE_SESSION_KEY = "django_language"


def set_language(request, language_code):
    if language_code in dict(settings.LANGUAGES):
        activate(language_code)

        request.session[LANGUAGE_SESSION_KEY] = language_code

        response = HttpResponseRedirect(request.GET.get("next", "/"))
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language_code)
        return response

    return HttpResponseRedirect(request.GET.get("next", "/"))
