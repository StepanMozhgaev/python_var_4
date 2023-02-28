import os
import re


def next_element(path: str) -> str | None:
    """
    :param path: path to image
    :return: path to next image
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


if __name__ == "__main__":
    print(next_element("C:\\Users\\0\\python_var_7\\dataset\\zebra\\0001.jpg"))
