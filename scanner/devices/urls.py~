from django.urls import include, path

from devices.view import DeviceViewSet, LocationViewSet
from dictionary.models import Device, Location

#app_name = 'device'
urlpatterns = [
    path(r'devices/scan', DeviceViewSet, name='devices'),
    path(r'locations/', LocationViewSet, name='locations'),
]
