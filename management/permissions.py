from rest_framework import permissions
from rest_framework import authentication
from management.models import *


class CategoryPermissions(permissions.IsAuthenticated):


    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        elif request.method in ('HEAD', 'OPTIONS', 'GET'):
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        elif request.method in ('HEAD', 'OPTIONS', 'GET'):
            return True
        return False


class AdvertisementPermission(permissions.IsAuthenticated):

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        elif request.user.is_authenticated:
            return True
        elif request.method in ('HEAD', 'OPTIONS', 'GET',):
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if obj.user == request.user or request.user.is_superuser:
            return True
        elif request.method in ('HEAD', 'OPTIONS', 'GET',):
            return True
        return False