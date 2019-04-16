import json

from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response


class ApiRenderer(JSONRenderer):
    """Custom renderer for all Api views"""
    
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        return json.dumps(data)
