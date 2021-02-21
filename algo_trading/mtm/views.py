from django.http import JsonResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView

from .mtm_service import simple_momentum


# function-based view
# def simple_momentum_view(request, ticker, span):
#     return HttpResponse(json.dumps(simple_momentum(ticker, span, offset=0)))


class SimpleMomentumView(APIView):
    """
    Momentum class-based view with swagger configured
    """
    @swagger_auto_schema(
        operation_description='Get Simple Momentum given ticker & span',
        tags=['Momentum', 'Crypto']
    )
    def get(self, request, ticker, span):
        return JsonResponse(
            {
                f'mtm-{ticker}-{span}': simple_momentum(ticker, span, offset=0)
            }
        )
