from datetime import datetime
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from campaigns.choices import ACCEPTANCE_STATUS_CHOICES
from campaigns.models import Campaign

class Event(models.Model):
    name = models.CharField(_("name"), max_length=255, null=False, blank=True)
    slug = models.SlugField(_("slug"), unique=True, null=False, blank=True)
    campaign = models.ForeignKey(Campaign, verbose_name=_("campaign"), on_delete=models.CASCADE, related_name="opportunities", null=False, blank=True)
    attendees = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name=_("attendees"), through="Attendee", related_name="events", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _("event")
        verbose_name_plural = _("events")
        
    def save(self, *args, **kwargs):
        today = datetime.today()
        slugified = slugify(self.name)
        self.slug = f'{slugified}-{today:%Y%m%d%M%S%f}'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("event_detail", kwargs={"pk": self.pk})

class Attendee(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("user"), on_delete=models.CASCADE, blank=True)
    event = models.ForeignKey(Event, verbose_name=_("event"), on_delete=models.CASCADE, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _("attendee")
        verbose_name_plural = _("attendee")

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("volunteer_detail", kwargs={"pk": self.pk})
    
class Invite(models.Model):
    label = models.CharField(_("label"), max_length=255, null=False, blank=True)
    status = models.CharField(_("status"), max_length=14, choices=ACCEPTANCE_STATUS_CHOICES, default="Pending", blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("user"), on_delete=models.CASCADE, related_name="invites", blank=True)
    event = models.ForeignKey(Event, verbose_name=_("event"), on_delete=models.CASCADE, related_name="invites", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("invite")
        verbose_name_plural = _("invites")

    def __str__(self):
        return self.label

    def get_absolute_url(self):
        return reverse("invite_detail", kwargs={"pk": self.pk})
