import os
import re


def next_element(path: str) -> str | None:
    """"
    принимает на вход путь к файлу, возвращает путь к следующему файлу, если файла не сущ.,
    то возвращает "Такого файла не существует", если последний файл, то возвращает None
    path - путь к файлу
    """
    if os.path.isfile(path):
        directory, filename = os.path.split(path)
        index = re.search(r'\d{4}', filename)
        ind = int(index.group(0))
        ind += 1
        if ind < 1000:
            next_elem = os.path.join(directory, re.sub(r'\d{4}', f'{ind:04d}', filename))
            return next_elem
        else:
            return None
    else:
        return "No files found"
