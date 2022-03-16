import requests
import time
from datetime import datetime
from progress.bar import IncrementalBar


class VkApi:
    def __init__(self, name):
        self.name = name

    def check_input(self, url_info):
        if 'error' in url_info.keys():
            print(url_info['error']['error_msg'])
            return False
        elif 'DELETED' in url_info['response'][0]['first_name']:
            print(f"The user's ID access is deleted")
            return False
        elif url_info['response'][0]['is_closed']:
            print(f"The user's ID access is closed")
            return False
        else:
            return True

    def input_id_token(self):
        while True:
            input_id = input(f'Please enter Id from {self.name}: ')
            input_token = input(f'Please enter Token from {self.name}: ')
            url = 'https://api.vk.com/method/users.get'
            params = {
                'user_ids': input_id,
                'access_token': input_token,
                'v': '5.131'
            }
            get_info = requests.get(url, params).json()
            if self.check_input(get_info):
                id = get_info['response'][0]['id']
                return id, input_token

    def get_photo_info(self, ):
        id, token = self.input_id_token()
        url = 'https://api.vk.com/method/photos.get'
        params_photo = {
            'owner_id': id,
            'access_token': token,
            'v': '5.131',
            'album_id': 'profile',
            'extended': '1'}
        photo_get = requests.get(url, params_photo).json()
        return photo_get['response']

    def get_list_photo(self):
        lists_photo = self.get_photo_info()
        bar = IncrementalBar('Get photo', max=100)
        photo_dict = {}
        for photo in lists_photo['items']:
            if photo_dict == {}:
                photo_dict = [{
                    'id': photo['id'],
                    'date': self.format_date(photo['date']),
                    'file_name': str(photo['likes']['count']),
                    'url': photo['sizes'][-1]['url'],
                    'size': photo['sizes'][-1]['type']}]
            else:
                photo_dict += [{
                    'id': photo['id'],
                    'date': self.format_date(photo['date']),
                    'file_name': str(photo['likes']['count']),
                    'url': photo['sizes'][-1]['url'],
                    'size': photo['sizes'][-1]['type']}]
            bar.next(100 / len(lists_photo['items']))
            time.sleep(0.1)
        bar.finish()
        print('Success get list photos')
        return photo_dict

    def format_date(self, date_int):
        date_int = datetime.fromtimestamp(date_int)
        date_int = date_int.strftime("-%d_%m_%Y_")
        return date_int
