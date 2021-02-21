import json

from django.http import JsonResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView

from signal_detector.signal_detector_service import get_all_alerts


class SignalDetectorView(APIView):
    """
    Signal detector view, returns all available alerts
    """
    @swagger_auto_schema(
        operation_description='Get all trading signal detected',
        tags=['Detector', 'Crypto']
    )
    def get(self, request):
        return JsonResponse(get_all_alerts(), safe=False)
