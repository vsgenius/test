from vkapi import VkApi
from yandexdiskapi import YandexDiskApi

def main():
    vk = VkApi('VK')
    vk_list_photo = vk.get_list_photo()
    ya = YandexDiskApi('Yandex')
    ya.upload_photo(vk_list_photo)


if __name__ == '__main__':
    main()
