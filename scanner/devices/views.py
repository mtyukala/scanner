import logging

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
from settings import GOOGLE_API_KEY

logger = logging.logger('__name')


class DeviceViewSet(ModelViewSet):
    """Documentation for DeviceViewSEt
    """
    render_class = (JSONRenderer,)
    context_object_name = 'devices'


class LocationViewSet(ModelViewSet):
    """
    """
    render_class = (JSONRenderer,)
    context_object_name = 'locations'
    serializer_class = LocationSerialzer
    permission_classes = (AllowAny)

    @action(methods='post')
    def get_location(self, request):
        pass

    def create(self, request):
        device_info = request.POST
        url = 'https://www.googleapis.com/geolocation/v1/geolocate?key={}'.format(
            GOOGLE_API_KEY)

        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # do your thing here
        return super().create(request)
