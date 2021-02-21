from django.apps import AppConfig


class SignalDetectorConfig(AppConfig):
    """
    Configure app name due to it has model and need to be added into settings.py
    """
    name = 'signal_detector'
