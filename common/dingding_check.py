#python 3.8
import time
import hmac
import hashlib
import base64
import urllib.parse

def dingding_check(secret):
    timestamp = str(round(time.time() * 1000))
    secret_enc = secret.encode('utf-8')
    string_to_sign = '{}\n{}'.format(timestamp, secret)
    string_to_sign_enc = string_to_sign.encode('utf-8')
    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
    return timestamp,sign


if __name__ == '__main__':
    dingding_check('SECea7f88d91f8b6a7a3ed0cb34a88fc6669c8094ad636d8df38dfa76a750f00901')
