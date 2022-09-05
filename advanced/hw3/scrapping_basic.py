
from bs4 import BeautifulSoup as bs
import requests
from fake_headers import Headers

url = 'https://habr.com/ru/all/'
KEYWORDS = ['QA', 'IP', 'Как', 'python']


def if_in_keywords(keywords, preview, header) :
    for key in KEYWORDS :
        if key in preview or key in header:
            print(key)
            return True


def get_link(url) :
    headers = Headers(browser="chrome", os="mac", headers=True).generate()
    response = requests.get(url, headers=headers)

    soup = bs(response.text, 'html.parser')
    elements = soup.find_all('div', class_="tm-article-snippet")
    return elements


def get_result() :
    elements = get_link(url)
    for element in elements :
        try :
            preview = element.find(class_='article-formatted-body article-formatted-body article-formatted-body_version-2')
            date = element.find('time')
            header = element.find(class_='tm-article-snippet__title-link')
            link = element.find(class_='tm-article-snippet__title-link').get('href')
            if if_in_keywords(KEYWORDS, preview.text, header.text) :
                print(f'{date.text} --- {header.text} --- {url[:-5] + link}')
        except :
            continue


def main() :
    get_result()


if __name__ == '__main__' :
    main()

