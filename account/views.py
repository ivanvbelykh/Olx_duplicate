# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from account.serializers import UserSerializer
from account.permissions import UserPermissions
from account.models import User

class UserViewSet(viewsets.ModelViewSet):
	"""User API view"""
 
	serializer_class = UserSerializer
	queryset = User.objects.all()
	permission_classes = (UserPermissions,)

