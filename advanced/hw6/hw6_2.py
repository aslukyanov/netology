
import requests
import json


def get_token(token_path) :
    with open(token_path, 'r') as file :
        return file.read()


def create_folder(folder, token_path) :
    token = get_token(token_path)
    URL = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {'Content-Type': 'application/json',
        'Accept': 'application/json', 
        'Authorization': f'OAuth {token}'}
    response = requests.put(f'{URL}?path={folder}', headers=headers)

    return response.status_code



if __name__ == '__main__':
    print(create_folder('test1', 'ya_token'))





