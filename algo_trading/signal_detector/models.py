from django.db import models


class Signal(models.Model):
    """
    Signal model (Entity): Data schema to store trading signal in database
    """
    DECISIONS = (
        ('B', 'Buy'),
        ('S', 'Sell'),
    )
    sid = models.AutoField(primary_key=True)  # primary sid: auto increasing
    signal_source = models.CharField(max_length=50)  # signal source: which algo triggered this signal
    security_name = models.CharField(max_length=20)  # security name: ticker
    decision = models.CharField(max_length=20, choices=DECISIONS)  # decision: buy or sell (enum)
    timestamp = models.DateTimeField(auto_now=True)  # time field to record when this signal happened
