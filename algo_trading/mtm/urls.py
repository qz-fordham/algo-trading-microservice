from django.urls import path

from . import views

# Routing
urlpatterns = [
    # path('<str:ticker>/<int:span>/', views.simple_momentum_view, name='mtm'),
    path('<str:ticker>/<int:span>/', views.SimpleMomentumView.as_view(), name='smtm'),
]
