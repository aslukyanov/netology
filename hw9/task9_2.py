

import requests
import json


class YaUploader:
    def __init__(self, token: str):
        self.token = token
        self.URL = 'https://cloud-api.yandex.net/v1/disk/resources'
        self.headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {self.token}'}


    def _get_temp_link(self, current_file_path: str, remote_file_path : str) :
        self._folder = remote_file_path + current_file_path.split("/")[-1]
        try :
            self.responce = requests.get(f'{self.URL}/upload?path={self._folder}&overwrite=True', headers=self.headers).json()
            return self.responce
        except :
            print(f"Error during getting temp link {self.responce}")
            

    def upload(self, current_file_path: str, remote_file_path : str):
        self.current_file_path = current_file_path
        self.remote_file_path = remote_file_path

        with open(self.current_file_path, 'rb') as f:
            try:
                requests.put(self._get_temp_link(self.current_file_path, self.remote_file_path)['href'], files={'file':f})
            except :
                print("Error in upload")
        print(f"File {self.current_file_path} has been sucessfully uploaded")


def read_my_token(path) :
    try :
        with open(path, "r") as file :
            token = file.read().strip()
    except Exception as ex :
        print(ex)
        return
    return token


if __name__ == '__main__':
    path_to_file = "/home/andrey/git/netology_test/hw_black_ver/test_file.txt"
    yandex_folder = "/api_test_upload/"
    token = read_my_token("/home/andrey/git/netology_test/hw_black_ver/yandex_token.txt")
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file, yandex_folder)


