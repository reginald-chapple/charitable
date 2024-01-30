from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from campaigns.models import Campaign

class Donation(models.Model):
    donor = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("donor"), on_delete=models.CASCADE, related_name="donations", null=False, blank=True)
    campaign = models.ForeignKey(Campaign, verbose_name=_("campaign"), on_delete=models.CASCADE, related_name="donations", null=False, blank=True)

    class Meta:
        verbose_name = _("donation")
        verbose_name_plural = _("donations")

    def __str__(self):
        return self.donor.username

    def get_absolute_url(self):
        return reverse("donation_detail", kwargs={"pk": self.pk})
