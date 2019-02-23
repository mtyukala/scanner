import json
import logging

import requests
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.utils.translation import ugettext as _
from django.views.generic import DetailView

from devices.models import Device, Location

logger = logging.getLogger('__name__')

ADRESS = 'https://www.googleapis.com/geolocation/v1/geolocate?key={}'
URL = ADRESS.format(settings.GOOGLE_API_KEY)


class LocationDetailView(DetailView):
    template_name = 'home.html'

    def post(self, request, *args, **kwargs):
        data = self.request.POST
        try:
            response = requests.post(URL, json=data)
            response.raise_for_status()

            if response.status_code is not 200:
                logger.error('Failed with {} error'.format(
                    response.status_code))
                return render(request, 'Failed with {} error'.format(response.status_code))

            if request.META['HTTP_ACCEPT'] == 'text/html':
                context = {"location": response.json()}
                return render(request, template_name=self.template_name, context=context)

            return JsonResponse(response.json())
        except requests.exceptions.HTTPError as e:
            logger.error("Http Error:", e)
        except requests.exceptions.ConnectionError as errc:
            logger.error("Error Connecting:", errc)
        except requests.exceptions.Timeout as errt:
            logger.error("Connection Timeout Error:", errt)
        except requests.exceptions.RequestException as err:
            logger.error("OOps: Something Else", err)

    def get(self, request, *args, **kwargs):
        return render(request, template_name=self.template_name)


def bad_request(request, exception, template_name="400.html"):
    response = render(template_name)
    response.status_code = 400
    return response


def permission_denied(request, exception, template_name="403.html"):
    response = render(template_name)
    response.status_code = 403
    return response


def handler404(request, exception, template_name="404.html"):
    response = render(template_name)
    response.status_code = 404
    return response


def handler500(request, exception, template_name='500.html'):
    response = render(template_name)
    response.status_code = 500
    return response
