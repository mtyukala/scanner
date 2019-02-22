import json
import logging

import requests
from django.conf import settings
from django.http import Http404, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.utils.translation import ugettext as _

from devices.models import Device, Location
from devices.serializers import DeviceSerialzer, LocationSerialzer
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
# Create your views here.
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

logger = logging.getLogger('__name__')

ADRESS = 'https://www.googleapis.com/geolocation/v1/geolocate?key={}'
URL = ADRESS.format(settings.GOOGLE_API_KEY)


class DeviceViewSet(ModelViewSet):
    """Documentation for DeviceViewSEt
    """
    render_class = (JSONRenderer,)
    context_object_name = 'devices'


class LocationViewSet(ModelViewSet):
    """
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerialzer
    render_class = (JSONRenderer,)
    context_object_name = 'locations'
    serializer_class = LocationSerialzer

    def create(self, request):
        data = request.POST
        response = requests.post(URL, json=data)
        response.raise_for_status()
        if response.status_code is not 200:
            logger.error('Failed with {} error'.format(response.status_code))
            return Response("", status=status.HTTP_400_BAD_REQUEST)
        return Response(response.json())
