import logging

from django.contrib.auth.models import Group, User
from django.db import transaction

from dictionary.models import Device, Location
from rest_framework import serializers

logger = logging.getLogger(__name__)


class DeviceSerialzer(serializers.ModelSerializer):
    """Documentation for DeviceSerialzer

    """
    class Meta:
        model = Device


class LocationSerialzer(serializers.ModelSerializer):
    """Documentation for DeviceSerialzer

    """
    class Meta:
        model = Location
