"""algo_trading URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import threading

from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from signal_detector.signal_detector_service import signal_detector_daemon
from .start_up import sign_in

sign_in()

# Swagger related code
schema_view = get_schema_view(
    openapi.Info(
        title='Algo Trading RESTful API',
        default_version='1.0',
        description='Demonstration of algo trading microservice restful api with swagger',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# Routing
urlpatterns = [
    path('admin/', admin.site.urls),
    path('ma/', include('ma.urls')),
    path('mtm/', include('mtm.urls')),
    path('detector/', include('signal_detector.urls')),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

# Start signal_detector as a daemon thread
t = threading.Thread(target=signal_detector_daemon, daemon=True)
t.start()
