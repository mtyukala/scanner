from django.urls import include, path

from devices.models import Device, Location
from devices.views import DeviceViewSet, LocationViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'scan', LocationViewSet, base_name='scan')
router.register(r'location', DeviceViewSet, base_name='loction')

#app_name = 'device'
urlpatterns = [
    #    path(r'api/v1/devices/', DeviceViewSet, name='devices'),
    #   path(r'scan/', LocationViewSet, name='locations'),
    path('', include((router.urls, 'devices'), namespace='devices')),
]
