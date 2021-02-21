class MTMException(BaseException):
    """
    MTM generic exception
    """
    def __init__(self, msg):
        print('Failed to get MTM: ' + msg)
