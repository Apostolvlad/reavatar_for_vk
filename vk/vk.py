# from vk import Vk
from .client import Client

class VkCaptcha(Exception): pass
class VkAuth(Exception): pass

class Vk: 
    def __init__(self, token):
        self._client = Client()
        
        self._token = token
        self._version = '5.103'
        
        self._captcha_sid = None

        self._params = {'access_token':self._token, 'v':self._version, 'captcha_sid':self._captcha_sid, 'captcha_key':None}
        self.user_id = self.get_id()

    def get(self, url, param = {}): return self.check_error(self._client.get(url, self.get_params(param)))

    def post(self, url, data = {}, files = {}): return self.check_error(self._client.post(url, data = self.get_params(data), files = self.get_params(files)))
    
    def check_error(self, result):
        response = result.get('response', False)
        if response: return response
        error = result.get('error', False)
        if not error: return result
        error_code = error.get('error_code')
        if error_code == 14:
            self._captcha_sid = error.get('captcha_sid')
            self._client.save_picture(error.get('captcha_img'), 'captch.png')
            raise VkCaptcha('CAP detected!!!')
        elif error_code == 5:
            raise VkAuth('Auth failed!!!')
        raise Exception(result)

    def set_code(self, code): self._params({'captcha_sid':self._captcha_sid, 'captcha_key':code})

    def get_params(self, param = None): 
        if param == None: return {}
        param.update(self._params)
        return param
    
    def get_id(self): return self.get('https://api.vk.com/method/users.get')[0].get('id')

    def loud_photo(self, owner_id, file):
        response = self.get('https://api.vk.com/method/photos.getOwnerPhotoUploadServer', {'owner_id':owner_id})
        response = self._client.post(response.get('upload_url'), files = {'file': file})
        return (response.get('server'), response.get('photo'), response.get('hash'))

    def set_photo(self, server, photo, hashs): 
        return self.post('https://api.vk.com/method/photos.saveOwnerPhoto', data = {'server':server, 'photo':photo, 'hash':hashs})

    def del_post(self, owner_id, post_id): return self.get('https://api.vk.com/method/wall.delete', {'post_id':post_id, 'owner_id':owner_id})