from django.http import JsonResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView

from .ma_service import simple_moving_average


# function-based view
# def sma_view(request, ticker, span):
#     return HttpResponse(json.dumps(simple_moving_average(ticker, span)))


class SMAView(APIView):
    """
    SMA class-based view with swagger configured
    """
    @swagger_auto_schema(
        operation_description='Get Simple Moving Average (SMA) given ticker & span',
        tags=['Moving Average', 'Crypto']
    )
    def get(self, request, ticker, span):
        return JsonResponse(
            {
                f'sma-{ticker}-{span}': simple_moving_average(ticker, span)
            }
        )
