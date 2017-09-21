# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    """user model"""
    phonenumber = models.PositiveIntegerField(null=True, blank=True)
