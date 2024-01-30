from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class Member(models.Model):
    identity = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name=_("identity"), on_delete=models.CASCADE, related_name="membership")
    

    class Meta:
        verbose_name = _("member")
        verbose_name_plural = _("members")

    def __str__(self):
        return self.identity.username

    def get_absolute_url(self):
        return reverse("member_detail", kwargs={"pk": self.pk})
