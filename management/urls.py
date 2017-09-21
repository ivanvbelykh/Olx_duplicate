from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as restview
from management.views import CategoryViewSet, AdvertisementViewSet

router = routers.DefaultRouter()
router.register(r'category', CategoryViewSet, 'category')
router.register(r'advertisement', AdvertisementViewSet, 'ad')
urlpatterns = [
]
urlpatterns += router.urls