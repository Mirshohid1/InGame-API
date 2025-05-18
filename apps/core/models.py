from django.db import models
from django.utils.translation import gettext_lazy as _

from .utils import clean_text_fields


class BaseModel(models.Model):
    created_at = models.DateTimeField(verbose_name=_('Created At'), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_('Updated At'), auto_now=True)

    def clean(self):
        for field in self._meta.fields:
            if (isinstance(field, models.CharField) or 
                isinstance(field, models.TextField) or
                isinstance(field, models.EmailField)
                ):
                value = getattr(self, field.name)
                setattr(self, field.name, clean_text_fields(value))
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    class Meta:
        abstract = True
