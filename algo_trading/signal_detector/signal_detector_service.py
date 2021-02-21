import json
import time
from datetime import datetime

from django.core.serializers import serialize

from algo_trading.portfolio import crypto
from mtm.mtm_service import simple_momentum_alert
from .models import Signal


def mtm_detector():
    """
    Trading signal detector using Momentum
    When signal is triggered, store it in the database
    :return: None
    """
    for ticker, span in crypto.items():
        signal = simple_momentum_alert(ticker, span)
        if signal == 1:
            historical = Signal.objects.filter(security_name=ticker, timestamp__date=datetime.now().date(),
                                               decision='B').order_by('-timestamp')
            last = None if not historical else historical[0]
            if not last:
                cur_signal = Signal(
                    signal_source='Momentum', security_name=ticker,
                    decision='B'
                )
                cur_signal.save()
        elif signal == -1:
            historical = Signal.objects.filter(security_name=ticker, timestamp__date=datetime.now().date(),
                                               decision='S').order_by('-timestamp')
            last = None if not historical else historical[0]
            if not last:
                cur_signal = Signal(
                    signal_source='Momentum', security_name=ticker,
                    decision='S'
                )
                cur_signal.save()


def signal_detector_daemon():
    """
    detector daemon executes every 10 seconds
    TODO: In future, if there are more signal detector, simply wrap around them and add them in this method
    :return: None
    """
    while True:
        mtm_detector()
        time.sleep(10)


def get_all_alerts():
    """
    Database query to get all trading signals
    :return: List of Signal entity queried from database
    """
    data = [record['fields'] for record in json.loads(serialize('json', Signal.objects.all()))]
    return data
