from vk import Vk, VkCaptcha

class Bot:
    def __init__(self, token):
        self._run = False
        self._vk = Vk(token)
    
    def start(self):
        pass







    def run(self): self._run = True
    def stop(self): self._run = False