import os
import csv


default = ["zebra", "bay horse"] # дефолтные классы


class Data:
    def __init__(self, directory: str) -> None:
        self.directory = directory
        self.str_num = 0
    """
    self.str_num - кол-во строк в аннотации
    """

    def adder(self, path: str, class_name: str, img_name: str) -> None:
        """
        path - путь к директории
        class_name - имя дефолтного класса
        img_name - имя изображения
        функция записывает в файл-аннотацию информацию об изображении
        """
        with open(os.path.join(path, self.directory, "annotation.csv"), "a", encoding="utf-8", newline="") as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            while self.str_num == 0:
                writer.writerow([
                    "Absolute path",
                    "Relative path",
                    "Class"
                ])
                """
                если кол-во строк равно 0, то заголовок
                """
                self.str_num += 1
            writer.writerow([os.path.join(path, self.directory, class_name, img_name),
                             os.path.join(self.directory, class_name, img_name), class_name])
            self.str_num += 1
