# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.db import models
from account.models import User

# Create your models here.
class Category(models.Model):
	"""Tasks Model"""
	
	category_name = models.CharField(max_length=50, null=True)
	def __str__(self):
		return u'%s' % (self.category_name)

class Advertisement(models.Model):
	"""Advertisement Model"""
	product_name = models.CharField(max_length=50, null=True)
	price = models.IntegerField(null=True)
	ad_date = models.DateTimeField(auto_now_add = True)
	category = models.ForeignKey(Category, null=True, blank=True)
	user = models.ForeignKey(User, null=True, blank=True)
	image = models.ImageField(upload_to='image/', null=True, blank=True)
	view_count = models.IntegerField(default=0)
	description = models.TextField(null=True)