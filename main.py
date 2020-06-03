from vk import *
from bot import Bot

def main():
    try:
        vk = Vk('') # токен
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
