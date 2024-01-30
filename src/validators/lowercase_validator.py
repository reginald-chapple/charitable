from django.core import validators
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _

@deconstructible
class LowercaseValidator(validators.RegexValidator):
    regex = r'^[a-z][a-z0-9_]+$'
    message = _('Enter a valid value. This value may contain only lowercase letters, numbers, and underscores. Must start with a letter.')
    flags = 0