from vk import *
from bot import Bot

def main():
    try:
        vk = Vk('e083800fd2546e1fa614699a8757923d92adca1e0dd9c7a814131736344eb2eeea907aef1233e1792727a') #
    except VkAuth:
        return 1
    b = Bot(vk, vk.user_id, 60)
    b.run()
    try:
        b.start('avatars')
    except VkCaptcha:
        print('cap')


if __name__ == "__main__":
    main()