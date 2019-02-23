from django.conf.urls import handler400, handler403, handler404, handler500
from django.urls import include, path

from devices.views import DeviceViewSet, LocationDetailView, LocationView

handler400 = 'devices.views.bad_request'
handler403 = 'devices.views.permission_denied'
handler404 = 'devices.views.handler404'
handler500 = 'devices.views.handler500'

urlpatterns = [
    path(r'scan/', LocationDetailView.as_view(), name='location'),
]
