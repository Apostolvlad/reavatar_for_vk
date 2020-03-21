# from vk import Vk
from client import Client

class VkCaptcha(Exception): pass

class Vk: 
    def __init__(self, token):
        self._client = Client()
        self._token = token
        self._version = '5.103'
        
        self._captcha_sid = None
        self._captcha_key = None
        self._params = {'access_token':self._token, 'v':self._version, 'captcha_sid':self._captcha_sid, 'captcha_key':self._captcha_key}

    def get_params(self, **param): 
        param.update(self._params)
        return param

    def check_error(self, result):
        response = result.get('response', False)
        if response: return response
        error = result.get('error')
        error_code = error.get('error_code')
        if error_code == 14:
            self._captcha_sid = error.get('captcha_sid')
            self._vk.client.save_picture(error.get('captcha_img'), 'captch.png')
            raise VkCaptcha('CAP detected!!!')
        raise Exception(result)
    
    def get(self, url, param): return self.check_error(self._client.get(url, self.get_params(param)))

    def post(self, url, param): return self.check_error(self._client.post(url, self.get_params(param)))
    
    def loud_photo(self, owner_id, file):
        response = self.get('https://api.vk.com/method/photos.getOwnerPhotoUploadServer', {'owner_id':owner_id})
        response = self.post(response.get('upload_url'), files = {'file': file})
        return (response.get('server'), response.get('photo'), response.get('hash'))
    
    def set_photo(self, server, photo, hashs): return self.post('https://api.vk.com/method/photos.saveOwnerPhoto', {'server':server, 'photo':photo, 'hash':hashs})

    def del_post(self, owner_id, post_id): return self.get('https://api.vk.com/method/wall.delete', self.get_params(post_id = post_id, owner_id = owner_id))
