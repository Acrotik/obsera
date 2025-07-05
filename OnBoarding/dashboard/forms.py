from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate
from .models import CustomUser
from django.utils.translation import gettext_lazy as _


class EmailAuthenticationForm(forms.Form):
    error_messages = {
        "invalid_login": _("Error : Please enter a valid email or password"),
        "inactive": _("This account is inactive."),
    }
    username = forms.EmailField(
        label="Email", widget=forms.EmailInput(attrs={"autofocus": True})
    )
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        email = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if email and password:
            user = authenticate(self.request, username=email, password=password)
            if user is None:
                raise forms.ValidationError(self.error_messages["invalid_login"])
            elif not user.is_active:
                raise forms.ValidationError(self.error_messages["inactive"])
            else:
                self.user_cache = user

        return self.cleaned_data


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("email", "name", "lastname", "phone", "address")


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("email", "name", "lastname", "phone", "address")
