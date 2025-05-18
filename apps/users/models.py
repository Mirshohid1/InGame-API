from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField

from core.models import BaseModel
from .managers import UserManager


class Role(BaseModel):
    name = models.CharField(max_length=100, unique=True, verbose_name=_("name"))
    
    def __str__(self):
        return self.name


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    first_name = models.CharField(max_length=100, blank=True,verbose_name=_('first name'))
    last_name = models.CharField(max_length=100, blank=True, verbose_name=_('last name'))
    email = models.EmailField(unique=True, blank=True, verbose_name=_('email address'))
    password = models.CharField(max_length=128, verbose_name=_('password'))
    phone = PhoneNumberField(unique=True, null=True, blank=True, region='UZ')
    roles = models.ManyToManyField(Role, related_name='users', blank=True, verbose_name=_('roles'))
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email or f"User #{self.pk}"
