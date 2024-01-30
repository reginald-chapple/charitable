from datetime import datetime
from django.conf import settings
from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from campaigns.choices import ACCEPTANCE_STATUS_CHOICES
from campaigns.models import Campaign

class Opportunity(models.Model):
    title = models.CharField(_("title"), max_length=255, null=False, blank=True)
    slug = models.SlugField(_("slug"), unique=True, null=False, blank=True)
    campaign = models.ForeignKey(Campaign, verbose_name=_("campaign"), on_delete=models.CASCADE, related_name="opportunities", null=False, blank=True)
    volunteers = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name=_("volunteers"), through="Volunteer", related_name="opportunities", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _("opportunity")
        verbose_name_plural = _("opportunities")
        
    def save(self, *args, **kwargs):
        today = datetime.today()
        slugified = slugify(self.title)
        self.slug = f'{slugified}-{today:%Y%m%d%M%S%f}'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("opportunity_detail", kwargs={"pk": self.pk})

class Volunteer(models.Model):
    status = models.CharField(_("status"), max_length=14, choices=ACCEPTANCE_STATUS_CHOICES, default="Pending", blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("user"), on_delete=models.CASCADE, blank=True)
    opportunity = models.ForeignKey(Opportunity, verbose_name=_("opportunity"), on_delete=models.CASCADE, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _("volunteer")
        verbose_name_plural = _("volunteers")

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("volunteer_detail", kwargs={"pk": self.pk})
