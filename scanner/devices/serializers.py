import logging

from django.contrib.auth.models import Group, User
from django.db import transaction

from devices.models import Device, Location
from rest_framework import serializers

logger = logging.getLogger(__name__)


class DeviceSerialzer(serializers.ModelSerializer):
    """Documentation for DeviceSerialzer

    """
    class Meta:
        model = Device
        fields = '__all__'


class LocationSerialzer(serializers.ModelSerializer):
    """Documentation for DeviceSerialzer

    """
    class Meta:
        model = Location
        fields = '__all__'
