import robin_stocks as rbh

from ma.exceptions import SMAException


def simple_moving_average(ticker, span):
    """
    Calculate simple moving average (SMA) given Cryptocurrency ticker and span
    :param ticker: itr -> Cryptocurrency ticker
    :param span: int -> Time span
    :return: float -> SMA
    """
    try:
        historical_prices = rbh.crypto.get_crypto_historicals(ticker, 'day', 'year')
        close_prices = [float(price['close_price']) for price in historical_prices[-span:]]
        return round(sum(close_prices) / span, 2)
    except Exception as e:
        raise SMAException(e.__str__())
