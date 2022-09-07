
from datetime import datetime
from bs4 import BeautifulSoup as bs
import requests
from fake_headers import Headers


class ClassLoggerDecorator:

    def __init__(self, path):
        self.path = path

    def __call__(self, func, *args, **kwargs):
        def inner_func(*args, **kwargs):
            start_func_time = datetime.now()
            result = func(*args, **kwargs)
            with open(self.path, 'a') as file :
                file.write(f'#########################################\n')
                file.write(f'Fuction started at {start_func_time}\n')
                file.write(f"Function name is {func.__name__}\n")
                file.write(f"Aguments of function are {args} {kwargs}\n")
                file.write(f'#########################################\n')
                file.write(f'Result of executed function is {result}\n')
                file.write(f'#########################################\n')
            return result
        return inner_func


def logger_dec(path : str) :
    def dec(func) :
        def wrapped(*args, **kwargs) :
            start_func_time = datetime.now()
            result = func(*args, **kwargs)
            with open(path, 'a') as file :
                file.write(f'#########################################\n')
                file.write(f'Fuction started at {start_func_time}\n')
                file.write(f"Function name is {func.__name__}\n")
                file.write(f"Aguments of function are {args} {kwargs}\n")
                file.write(f'#########################################\n')
                file.write(f'Result of executed function is {result}\n')
                file.write(f'#########################################\n')
            return result
        return wrapped
    return dec


@logger_dec('./logs.txt')
def get_link_v1(url : str) :
    headers = Headers(browser="chrome", os="mac", headers=True).generate()
    response = requests.get(url, headers=headers)

    soup = bs(response.text, 'html.parser')
    elements = soup.find_all('div', class_="tm-article-snippet")
    return elements[0]


@ClassLoggerDecorator('./logs.txt')
def get_link_2(url) :
    headers = Headers(browser="chrome", os="mac", headers=True).generate()
    response = requests.get(url, headers=headers)

    soup = bs(response.text, 'html.parser')
    elements = soup.find_all('div', class_="tm-article-snippet")
    return elements[0]


if __name__ == '__main__' :
    url = 'https://habr.com/ru/all/'
    # get_link_v1(url)
    get_link_2(url)






















