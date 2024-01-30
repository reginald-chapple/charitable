from datetime import datetime
from django.conf import settings
from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from campaigns.models import Cause

class Campaign(models.Model):
    name = models.CharField(_("name"), max_length=255, null=False, blank=True)
    slug = models.SlugField(_("slug"), unique=True, null=False, blank=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("creator"), on_delete=models.CASCADE, related_name="campaigns", null=False, blank=True)
    cause = models.ForeignKey(Cause, verbose_name=_("cause"), on_delete=models.CASCADE, related_name="campaigns", null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _("campaign")
        verbose_name_plural = _("campaigns")
        
    def save(self, *args, **kwargs):
        today = datetime.today()
        slugified = slugify(self.name)
        self.slug = f'{slugified}-{today:%Y%m%d%M%S%f}'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("campaign_detail", kwargs={"pk": self.pk})
