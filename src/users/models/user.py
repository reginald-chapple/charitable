import uuid
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from validators import LowercaseValidator
from users.choices import USER_GENDER_CHOICES
from users.managers import AppUserManager

class User(AbstractUser):
    # fields removed from base user model
    first_name = None
    last_name = None
    username = models.CharField(
        _('user name'),
        max_length=30,
        unique=True,
        help_text=_('Required. 30 characters or fewer. Lowercase letters, numbers, and @/./+/-/_ only.'),
        validators=[LowercaseValidator()],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
         null=False, 
         blank=True
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(_('email address'), unique=True, blank=True)
    name = models.CharField(_('full name'), max_length=255, blank=True)
    phone_number = models.CharField(
        _("phone number"),
        max_length=16,
        blank=True,
        null=True,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="Phone number must be entered in the format '+123456789'. Up to 15 digits allowed."
            ),
        ],
    )
    birthdate = models.DateField(_("birthdate"), auto_now=False, auto_now_add=False, null=True, blank=True)
    gender = models.CharField(_("gender"), max_length=14, choices=USER_GENDER_CHOICES, null=True, blank=True)
    photo = models.ImageField(_("photo"), upload_to='members/%Y/%m/%d/', null=True, blank=True)
    address = models.CharField(_("address"), max_length=50, null=True, blank=True)
    city = models.CharField(_("city"), max_length=50, null=True, blank=True)
    country = models.CharField(_("country"), max_length=50, null=True, blank=True)
    state = models.CharField(_("state"), max_length=50, null=True, blank=True)
    zip = models.CharField(_("zip"), max_length=12, null=True, blank=True)
    is_member = models.BooleanField(_('member status'), default=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name','email',]

    objects = AppUserManager()

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return self.username
