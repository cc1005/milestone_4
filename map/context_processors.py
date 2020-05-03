import os
from django.conf import settings

def add_variable_to_context(request):
    return {
        'map_api': os.environ.get('MAPS_API_KEY')
    }