from __future__ import unicode_literals
from django.shortcuts import get_object_or_404
from django.db.models import F
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from management.serializers import CategorySerializer, AdvertisementSerializer, AdvertisementCreateSerializer
from management.permissions import CategoryPermissions, AdvertisementPermission
from management.models import Category,Advertisement

class CategoryViewSet(viewsets.ModelViewSet):
	"""category Viewset allows to list edit create delet category"""
	serializer_class = CategorySerializer
	queryset = Category.objects.all()
	permission_classes = (CategoryPermissions,)


class AdvertisementViewSet(viewsets.ModelViewSet):
	"""advertisemnet viewset allow us to list edit create delete 
	advertisement"""
	queryset = Advertisement.objects.all()
	serializer_class = AdvertisementSerializer
	filter_backends = (SearchFilter, DjangoFilterBackend) 
	search_fields = ['product_name', 'category__category_name',]
	permission_classes = (AdvertisementPermission,)

	def get_serializer_class(self):
		if self.request.method != 'GET': 
			self.serializer_class = AdvertisementCreateSerializer 
		return self.serializer_class

	def retrieve(self, request, pk=None):
		queryset = Advertisement.objects.all()
		advertisement = get_object_or_404(queryset, pk=pk)
		Advertisement.objects.filter(pk=pk).update(view_count=F('view_count') + 1)
		advertisement.view_count += 1 
		serializer = AdvertisementSerializer(advertisement)
		return Response(serializer.data)

