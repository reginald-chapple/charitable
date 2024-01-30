from datetime import datetime
from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from campaigns.models import Campaign

class Expenditure(models.Model):
    item =  models.CharField(_("item"), max_length=255, null=False, blank=True)
    slug = models.SlugField(_("slug"), unique=True, null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _("expenditure")
        verbose_name_plural = _("expenditures")
        
    def save(self, *args, **kwargs):
        today = datetime.today()
        slugified = slugify(self.item)
        self.slug = f'{slugified}-{today:%Y%m%d%M%S%f}'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.item

    def get_absolute_url(self):
        return reverse("expenditure_detail", kwargs={"pk": self.pk})
