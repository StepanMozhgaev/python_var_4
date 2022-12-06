import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import time


urls = []


def create_dir():
    path = 'C:/Users/0/python_var_7/Lab1'
    folders = ['zebra', 'bay horse']

    if not os.path.exists(path):
        os.mkdir(path)

    for f in folders:
        folder = os.path.join(path, f)
        if not os.path.exists(folder):
            os.mkdir(folder)


"""
func creates directory if it doesn't exists
"""


def is_valid(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)


"""
func checks if image's url valid
"""


def get_all_images(url):
    print(url)
    html_page = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    html = BeautifulSoup(html_page.content, "html.parser")
    for img in html.find_all("img"):
        img_url = img.attrs.get("src")
        if not img_url:
            continue
        img_url = urljoin(url, img_url)
        print(img_url)
        if is_valid(img_url):
            urls.append(img_url)
            time.sleep(1)
    return urls


"""
func takes all images' urls from the page of yandex images and returns them into urls[]
"""


def download(url, pathname):
    global i
    request_img = requests.get(url)
    save = open(pathname + "/" + str(i).zfill(4) + ".jpg", "wb")
    i += 1
    save.write(request_img.content)
    save.close()


"""
func downloads image from the url and names it by pathname/0000, pathname/0001 etc. 
"""


def parce(url, path):
    imgs = get_all_images(url)
    for img in imgs:
        download(img, path)


"""
func takes urls from get_all_images and uses cycle to download them
"""


create_dir()


i = 0
page = 0
number = 0
directory_zebra = 'C:/Users/0/python_var_7/Lab1/zebra'


"""
zeroize i, page and number, because i is used for naming, page starts with 0 and number is number of files in tulip 
folder
"""


while number < 1050:
    url_zebra = 'https://yandex.by/images/search?p=' + str(page) + '&text=zebra'
    parce(url_zebra, directory_zebra)
    page += 1
    number = len(os.listdir(directory_zebra))
    urls = []
    time.sleep(10)


"""
func runs throw the pages of yandex images and downloads images
so, we increase page, clear urls and update number for correct work
time sleep func we use to avoid blocking because of too much requests to server
"""


i = 0
page = 0
number = 0
directory_bay_horse = 'C:/Users/0/python_var_7/Lab1/bay_horse'
while number < 1050:
    url_bay_horse = 'https://yandex.by/images/search?p=' + str(page) + '&text=bay horse'
    parce(url_bay_horse, directory_bay_horse)
    page += 1
    number = len(os.listdir(directory_bay_horse))
    urls = []
    time.sleep(10)


"""
everything is similarly to previous commit
"""
