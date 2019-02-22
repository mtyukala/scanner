from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext as _


# Create your models here.


class Device(models.Model):
    """
    Documentation for Device
    """
    band = models.CharField(max_length=10, verbose_name=_('Band'))
    bssid = models.CharField(max_length=30, verbose_name=_('BSSID'))
    channel = models.CharField(max_length=10, verbose_name=_('Channel'))
    frequency = models.IntegerField(verbose_name=_('Frequency'))
    rates = models.CharField(max_length=30, verbose_name=_('Rates'))
    rssi = models.IntegerField(verbose_name=_('RSSI'))
    security = models.CharField(max_length=10, verbose_name=_('Security'))
    ssid = models.CharField(max_length=50, verbose_name=_('SSID'))
    timestamp = models.DateTimeField(
        auto_now_add=True, verbose_name=_('Time Stamp'))
    vendor = models.CharField(max_length=50, verbose_name=_('Vendor'))
    width = models.CharField(max_length=5, verbose_name=_('Width'))

    class Meta:
        pass

    def get_absolute_url(self):
        return reverse('devices', args=[str(self.id)])

    def __str__(self):
        return "{} ({}, {})".format(self.vendor, self.bssid, self.ssid)


class Location(models.Model):
    """
    Documentation for Location
    """
    scan_file = models.FileField(max_length=40, verbose_name=_(
        'Upload file with device information'))
    latitude = models.DecimalField(decimal_places=1, max_digits=3)
    longitude = models.DecimalField(decimal_places=1, max_digits=3)
    accuracy = models.DecimalField(decimal_places=1, max_digits=5)

    class Meta:
        pass

    def get_absolute_url(self):
        return reverse('locations', args=[str(self.id)])
