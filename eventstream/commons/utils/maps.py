# -*- coding: utf-8 -*-
from googlemaps import GoogleMaps, GoogleMapsError

from django.conf import settings
from django.utils.encoding import smart_str

GOOGLE_MAPS_API_KEY = getattr(settings, 'GOOGLE_MAPS_API_KEY', '')

def get_lat_lng(address, silent=False):
    """
    address(unicode)からlat, lngを検索して返す
    silent = Trueだとエラーを出さない
    """
    addr_utf8 = smart_str(address)
    try:
        gmaps = GoogleMaps(GOOGLE_MAPS_API_KEY)
        lat, lng = gmaps.address_to_latlng(address)
    except GoogleMapsError:
        if silent:
            return None, None
        raise
    return lat, lng
