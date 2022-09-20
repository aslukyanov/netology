
import requests
from hw6_2 import *

class TestCreateYaFolder :

    def test_if_not_folder_exist(self) :
        token = get_token('./ya_token')
        URL = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = {'Content-Type': 'application/json',
        'Accept': 'application/json', 
        'Authorization': f'OAuth {token}'}
        response = requests.get(f'{URL}?path=test1', headers=headers).status_code
        assert response == 404


    def test_create_ya_folder(self) :
        assert create_folder('test1', './ya_token') == 201


    def test_if_folder_exist(self) :
        token = get_token('./ya_token')
        URL = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = {'Content-Type': 'application/json',
        'Accept': 'application/json', 
        'Authorization': f'OAuth {token}'}
        response = requests.get(f'{URL}?path=test1', headers=headers).status_code
        assert response == 200



