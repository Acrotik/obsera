from django import forms
from django.utils.translation import gettext_lazy as _

SERVICES_CHOICES = [
    ('Licensing', _('Licensing')),
    ('Security', _('Security')),
    ('Monitoring', _('Monitoring')),
    ('Cloud_Backup', _('Cloud Backup')),
    ('Consulting', _('Consulting')),
]


class ContactForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': _("Name"),
            'required': True,
            'style': 'border-radius: 8px; padding: 15px; width: 100%; box-sizing: border-box;',
        }),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'placeholder': _("Email"),
            'required': True,
            'style': 'border-radius: 8px; padding: 15px; width: 100%; box-sizing: border-box;',
        }),
    )
    phone = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            'placeholder': _("Phone"),
            'required': True,
            'style': 'border-radius: 8px; padding: 15px; width: 100%; box-sizing: border-box;',
        }),
    )
    company = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': _("Company"),
            'required': True,
            'style': 'border-radius: 8px; padding: 15px; width: 100%; box-sizing: border-box;',
        }),
    )
    message = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'placeholder': _("Message"),
            'style': 'border-radius: 8px; padding: 15px; width: 100%; box-sizing: border-box;',
        }),
    )

    services = forms.MultipleChoiceField(
        required=False,
        choices=SERVICES_CHOICES,
        widget=forms.CheckboxSelectMultiple(attrs={
            'style': 'margin-right: 10px;',
        }),
        label=_("Services Interested In"),
    )

    NB_EMPLOYEE_CHOICES = [
        ('0-5', '0-5'),
        ('6-15', '6-15'),
        ('15-50', '15-50'),
        ('50-100', '50-100'),
        ('100+', '100+'),
    ]

    nb_employee = forms.ChoiceField(choices=NB_EMPLOYEE_CHOICES, label=_('Nombre d\'employés'))
