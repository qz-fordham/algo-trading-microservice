class SMAException(BaseException):
    """
    SMA generic Exception
    """
    def __init__(self, msg):
        print('Failed to get SMA: ' + msg)
