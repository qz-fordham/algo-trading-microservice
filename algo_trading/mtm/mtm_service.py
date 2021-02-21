import robin_stocks as rbh

from mtm.exceptions import MTMException


def simple_momentum(ticker, span, offset=0):
    """
    Calculate momentum given ticker & span
    :param ticker: str -> ticker
    :param span: int -> time span
    :param offset: int -> date offset
    When offset = 0, meaning return the Momentum of today;
    when offset = 1, meaning return the Momentum of yesterday; and so on
    :return: Momentum
    """
    try:
        if span > 365:
            raise MTMException('Span cannot be greater than 365 days')
        historical_prices = rbh.crypto.get_crypto_historicals(ticker, 'day', 'year')
        momentum = \
            float(historical_prices[-(1 + offset)]['close_price']) \
            - float(historical_prices[-(span + offset)]['close_price'])
        return momentum
    except Exception as e:
        raise MTMException(e.__str__())


def simple_momentum_alert(ticker, span):
    """
    Check if there are trading signal for ticker using simple_momentum(ticker, span)
    :param ticker: str -> ticker
    :param span: int -> time span
    :return: 1 meaning 'buy' signal, -1 meaning 'sell' signal, 0 meaning do nothing
    """
    cur_price = float(rbh.crypto.get_crypto_quote(ticker)['mark_price'])
    prev_price = float(rbh.crypto.get_crypto_historicals(ticker, 'day', 'week')[-1]['close_price'])
    if simple_momentum(ticker, span) > simple_momentum(ticker, span, 1) and cur_price > prev_price:
        return 1  # buy signal
    elif simple_momentum(ticker, span) < simple_momentum(ticker, span, 1) and cur_price < prev_price:
        return -1  # sell signal
    else:
        return 0  # do nothing
