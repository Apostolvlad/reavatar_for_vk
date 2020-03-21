# from client import Client
import requests

class Client:
    def __init__(self, user_agent = None, timeout = 60): # 
        self._session = requests.Session() 
        if user_agent != None: self.session.headers.update({'User-Agent': user_agent})
        self._timeout = timeout

    def _get(self, url, params): return self._session.get(url, params = params, timeout = self._timeout)

    def _post(self, url, data = {}, files = {}): return self._session.get(url, data = data, files = files, timeout = self._timeout)
    
    def get(self, url, params = {}, json_mode = True):
        response = self._get(url, params)
        if json_mode: return response.json()
        return response.text

    def post(self, url, data = {}, files = {}, json_mode = True):
        response = self._post(url, params, files)
        if json_mode: return response.json()
        return response.text

    def save_picture(self, url, picture_name = 'picture.png'):
        response = self._get(url)
        out = open(picture_name, "wb")
        out.write(response.content)
        out.close()