from unittest.mock import DEFAULT
from . import models, serializers
from django.db.models import Prefetch, Q
from diana.abstract.views import DynamicDepthViewSet, GeoViewSet
from diana.abstract.models import get_fields, DEFAULT_FIELDS