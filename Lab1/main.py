import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

FOLDERS = ['zebra', 'bay_horse']
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                         "(KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
                         'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'one': 'true'}


def create_dir(path: str) -> None:
    """
    :param path: path to directory
    :return: none
    """
    try:
        os.mkdir(path)
    except OSError as err:
        print("OS error:", err)
    else:
        for f in FOLDERS:
            folder = os.path.join(path, f)
            try:
                os.mkdir(folder)
            except OSError as err:
                print("OS error:", err)


def is_valid(url: str) -> bool:
    """
    :param url: url of image
    :return: bool
    """
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)


def get_all_images(url: str) -> list:
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


def download(url: str, pathname: str, i: int) -> None:
    """
    :param url: url of image
    :param pathname: path to folder
    :param i: counter of names of files
    :return: none
    """
    request_img = requests.get(url)
    with open(os.path.join(pathname, str(i).zfill(4), ".jpg"), "wb") as save:
        save.write(request_img.content)


def parse(name: str, path: str, url: str = 'https://yandex.ru/images/', value: int = 1000) -> None:
    """
    :param value: number of images, we need to download
    :param url: yandex images
    :param name: searching name
    :param path: path to folder
    :return: none
    """
    i = 0
    page = 0
    while len(os.listdir(os.path.join(path, name))) < value:
        imgs = get_all_images(f"{url}search?p={str(page)}&text={name}")
        for img in imgs:
            download(img, os.path.join(path, name), i)
            i += 1
        page += 1
        print(f'Downloaded {i + 1} images')
    print(f'Process finished!')


if __name__ == "__main__":
    path: str = 'C:/Users/0/python_var_7/dataset'
    create_dir(path)
    parse(FOLDERS[0], path)
    parse(FOLDERS[1], path)
