import os.path
import requests
import time
import json
from progress.bar import IncrementalBar


class YandexDiskApi:
    list_file = []

    def __init__(self, name):
        self.name = name

    def get_headerss(self):
        while True:
            input_token = input(f'Please enter Token from {self.name}: ')
            headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {input_token}'}
            if self.check_token(input_token, headers):
                return headers

    def check_token(self, input_token, headers):
        url = 'https://cloud-api.yandex.net/v1/disk/'
        res = requests.get(url, headers=headers)
        code = res.status_code
        res = res.json()
        if 'message' in res.keys():
            # print('User authorization failed: no access_token passed.')
            return code
        return code

    def get_folder(self, path, headers):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/'
        res = requests.get(url, headers=headers, params={'path': path})
        if res.status_code == 404:
            requests.put(url, headers=headers, params={'path': path})
        return True

    def check_name(self, list_name, list_files):
        for list_file in list_files:
            if list_name + '.jpg' == list_file['file_name']:
                return True
        return False

    def get_href_list(self, url_photo, headers, path='Netology_CourseWork_1'):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload/'
        path = f'/{path}/'
        file_name = url_photo['file_name'] + '.jpg'
        file_name_with_date = str(url_photo['file_name']) + str(url_photo['date']) + '.jpg'
        if self.check_name(url_photo['file_name'], self.list_file):
            self.list_file += [{'file_name': file_name_with_date, 'size': url_photo['size']}]
            res = requests.get(url, headers=headers,
                               params={'path': path + file_name_with_date,
                                       'overwrite': True})
        else:
            self.list_file += [{'file_name': file_name, 'size': url_photo['size']}]
            res = requests.get(url, headers=headers,
                               params={'path': path + file_name, 'overwrite': True})
        self.json_file(self.list_file)
        return res.json()

    def json_file(self, list_file):
        data = json.dumps(list_file)
        with open('file.json', 'w') as f:
            f.write(data)

    def upload_photo(self, list_photo, path='Netology_CourseWork_1', count=5):
        self.get_folder(path, self.get_headerss())
        bar = IncrementalBar('Upload photos', max=100)
        num = 1
        for photo in list_photo:
            if num > count:
                break
            put_photo = requests.put(self.get_href_list(photo, headers)['href'], requests.get(photo['url']),
                                     headers=headers)
            bar.next(100 / count)
            if put_photo.status_code == 201:
                result = True
            else:
                result = False
            num += 1
            time.sleep(0.01)
        bar.finish()
        if not result:
            print('Files uploaded with errors')
            return
        print(f'The files were uploaded successfully to the {path} folder')
