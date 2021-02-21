from django.urls import path

from . import views

# Routing
urlpatterns = [
    # path('<str:ticker>/<int:span>/', views.sma_view, name='sma'),
    path('', views.SignalDetectorView.as_view(), name='detector'),
]
