from vk import VkCaptcha
from collections import OrderedDict
import time
import os
import random

class Bot:
    def __init__(self, vk, user_id, time, folder_name):
        self._run = False
        self._pause = False
        self._wait_code = False
        
        self._vk = vk
        self._user_id = user_id
        self._time = time
        self._folder_name = folder_name
        
        self._photo_base = self.loud_photo()

        self._i_max = len(self._photo_base) - 1
        self._i_photo = self._i_max
    
    def loud_photo(self): return OrderedDict(map(lambda x:{x:self._vk.loud_photo(self._user_id, open(f'{self._folder_name}\\{x}', 'rb'))}, os.listdir(self._folder_name)))

    @property
    def photo_names(self): return tuple(self._photo_base.keys())

    @property
    def photo_values(self): return tuple(self._photo_base.values())

    def get_photo(self): 
        if self._i_photo == self._i_max:
            random.shuffle(self._photo_base)
            self._i_photo = 0
        else:
            self._i_photo += 1
        return self.photo_values[self._i_photo]

    def job(self, photo):
        response = self._vk.set_photo(*photo)
        print(response)
        self._vk.del_post(self._user_id, response.get('post_id'))

    def start(self):
        ms = 0
        photo = self.get_photo()
        while self.is_run():
            if ms < time.time() and not self.is_code() and not self.is_pause():
                ms = time.time() + self._time
                try:
                    self.job(photo)
                    photo = self.get_photo()
                except VkCaptcha:
                    self._wait_code = True
            else:
                time.sleep(0.1)
    
    def run(self): self._run = not self._run

    def pause(self): self._pause = not self._pause

    def set_code(self, code):
        self._vk.set_code(code)
        self._wait_code = False

    def is_run(self): return self._run

    def is_pause(self): return self._pause

    def is_code(self): return self._wait_code