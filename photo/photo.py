

class Photo:
    def __init__(self, vk, user_id):
        self._vk = vk
        self._user_id = user_id

        self._picture_base = list()

    def add_picture(self, picture_name):
        self._picture_base.append(picture_name)

    def del_picture(self, picture_name):
        self._picture_base.remove(picture_name)

    def get_pictures(self):
        pass