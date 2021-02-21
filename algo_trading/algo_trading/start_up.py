import robin_stocks as rbh
import pyotp
from .settings import username, password


def sign_in():
    """
    Sign in to RobinHood to access data when server starts up
    :return: None
    """
    try:
        try:
            rbh.load_account_profile()
        except Exception as e:
            totp = pyotp.TOTP('My2factorAppHere').now()
            login = rbh.login(username, password, mfa_code=totp)
            print('sign in successfully')
            return login
    except Exception as e:
        print('fail login')
        print(e)
