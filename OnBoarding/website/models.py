from django.db import models
from django.utils.translation import gettext_lazy as _


class MyModel(models.Model):
    title = models.CharField(max_length=200, verbose_name=_("Title"))
    description = models.TextField(verbose_name=_("Description"))

    def __str__(self):
        return self.title