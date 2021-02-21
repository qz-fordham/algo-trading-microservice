from django.urls import path

from . import views

# Routing
urlpatterns = [
    # path('<str:ticker>/<int:span>/', views.sma_view, name='sma'),
    path('<str:ticker>/<int:span>/', views.SMAView.as_view(), name='sma'),
]
