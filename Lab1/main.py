import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

FOLDERS = ['zebra', 'bay_horse']
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                         "(KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
                         'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'one': 'true'}


def create_dir(path) -> None:
    """
    :param path: path to directory
    :return: none
    """
    try:
        os.mkdir(path)
    except OSError:
        print('Error: impossible to make directory')
    for f in FOLDERS:
        folder = os.path.join(path, f)
        try:
            os.mkdir(folder)
        except OSError:
            print('Error: impossible to make directory')


def is_valid(url) -> bool:
    """
    :param url: url of image
    :return: bool
    """
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)


def get_all_images(url) -> list:
    """
    :param url: url of yandex search
    :return: list
    """
    urls = []
    html_page = requests.get(url, HEADERS)
    html = BeautifulSoup(html_page.content, "html.parser")
    for img in html.find_all("img"):
        img_url = img.attrs.get("src")
        if not img_url:
            continue
        img_url = urljoin(url, img_url)
        if is_valid(img_url):
            urls.append(img_url)
    return urls


def download(url, pathname, i) -> None:
    """
    :param url: url of image
    :param pathname: path to folder
    :param i: counter of names of files
    :return: none
    """

    request_img = requests.get(url)
    with open(os.path.join(pathname, "/", str(i).zfill(4), ".jpg"), "wb") as save:
        save.write(request_img.content)
        save.close()


def parse(name, path='C:/Users/0/python_var_7/dataset/', url='https://yandex.ru/images/') -> None:
    """
    :param url: yandex images
    :param name: searching name
    :param path: path to folder
    :return: none
    """
    i = 0
    page = 0
    while len(os.listdir(os.path.join(path, name))) < 1000:
        imgs = get_all_images(f"{url}search?p={str(page)}&text={name}")
        for img in imgs:
            download(img, os.path.join(path, name), i)
            i += 1
        page += 1


if __name__ == "__main__":
    create_dir('C:/Users/0/python_var_7/dataset')
    parse(FOLDERS[0])
    parse(FOLDERS[1])
