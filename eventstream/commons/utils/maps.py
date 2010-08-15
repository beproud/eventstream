# -*- coding: utf-8 -*-
from googlemaps import GoogleMaps, GoogleMapsError

from django.conf import settings
from django.utils.encoding import smart_str

GOOGLE_MAPS_API_KEY = getattr(settings, 'GOOGLE_MAPS_API_KEY', '')
GOOGLE_MAPS_STATIC_IMAGE = 'http://maps.google.com/staticmap?zoom=%(zoom)s&center=%(lat)s,%(lng)s&size=%(size)s'
GOOGLE_MAPS_SEARCH = 'http://maps.google.com/?q=%(lat)s,%(lng)s(%(address)s)&z=%(zoom)s'
MAPS_IMAGE_SIZE_DEFAULT = getattr(settings, 'MAPS_IMAGE_SIZE_DEFAULT', (185, 185))

def get_lat_lng(address, silent=False):
    """
    address(unicode)からlat, lngを検索して返す
    silent = Trueだとエラーを出さない
    """
    addr_utf8 = smart_str(address)
    try:
        gmaps = GoogleMaps(GOOGLE_MAPS_API_KEY)
        lat, lng = gmaps.address_to_latlng(addr_utf8)
    except GoogleMapsError:
        if silent:
            return None, None
        raise
    return str(lat), str(lng)

def get_static_image_url(lat, lng, zoom=15, size=None):
    """
    staticmaps apiのURLを返す
    """
    params = {
        'lat': lat,
        'lng': lng,
        'zoom': zoom or '',
        'size': size or '%dx%d' % MAPS_IMAGE_SIZE_DEFAULT,
    }
    url = GOOGLE_MAPS_STATIC_IMAGE % params
    if GOOGLE_MAPS_API_KEY:
        url += '&key=%s' % GOOGLE_MAPS_API_KEY
    return url

def get_search_url(lat, lng, address, zoom=17):
    """
    mapsの検索結果へのURLを返す
    """
    params = {
        'lat': lat,
        'lng': lng,
        'address': address or '',
        'zoom': zoom or '',
    }
    return GOOGLE_MAPS_SEARCH % params
