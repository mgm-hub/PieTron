import urllib
import urllib2
import httplib
import requests


class HttpActions:
    def __init__(self):
        pass


    @staticmethod
    def get_page_response_code(my_url):
        try:
            return str(requests.head(my_url, allow_redirects=True).status_code)
        except StandardError:
            return None

