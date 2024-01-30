from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class Cause(models.Model):
    name = models.CharField(_("name"), max_length=255, null=False, blank=True)
    slug = models.SlugField(_("slug"), unique=True, null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("cause")
        verbose_name_plural = _("causes")
        
    def save(self, *args, **kwargs):
        slugified = slugify(self.name)
        self.slug = slugified
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("cause_detail", kwargs={"pk": self.pk})
