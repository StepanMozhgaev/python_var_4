import os
import shutil
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

folders = ['zebra', 'bay_horse']
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36", 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'one': 'true'}


def create_dir(path):
    try:
        os.mkdir(path)
    except OSError:
        shutil.rmtree(path)
        os.mkdir(path)

    for f in folders:
        folder = os.path.join(path, f)
        try:
            os.mkdir(folder)
        except OSError:
            shutil.rmtree(folder)
            os.mkdir(folder)


def is_valid(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)


def get_all_images(url):
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


def download(url, pathname, i):
    request_img = requests.get(url)
    with open(pathname + "/" + str(i).zfill(4) + ".jpg", "wb"):
        save = open(pathname + "/" + str(i).zfill(4) + ".jpg", "wb")
        save.write(request_img.content)
        save.close()


def parse(name):
    i = 0
    page = 0
    while len(os.listdir(os.path.join('C:/Users/0/python_var_7/dataset/', name))) < 1000:
        imgs = get_all_images(f"https://yandex.by/images/search?p=, {str(page)}, &text=, {name}")
        for img in imgs:
            download(img, os.path.join('C:/Users/0/python_var_7/dataset/', name), i)
            i += 1
        page += 1


if __name__ == "__main__":
    create_dir('C:/Users/0/python_var_7/dataset')
    parse('zebra')
    parse('bay_horse')
