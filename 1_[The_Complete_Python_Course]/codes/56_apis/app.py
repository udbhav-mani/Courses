import requests
from libs.openexchange import OpenExchangeLibrary

openid_client = OpenExchangeLibrary("beba5cc238614f208df88dc3d5cc8dab")

# openid_client.convert(10, "USD", "KRW")
openid_client.convert(10, "INR", "INR")
openid_client.convert(10, "INR", "USD")
