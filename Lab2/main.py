import os
import csv


default = ["zebra", "bay horse"] # дефолтные классы


class Data:
    def __init__(self, directory: str) -> None:
        """
        :param directory: dir for annotation file
        """
        self.directory = directory
        self.str_num = 0

    def adder(self, path: str, class_name: str, img_name: str) -> None:
        """
        :param path: new dir path
        :param class_name: class name
        :param img_name: image name
        """
        with open(os.path.join(path, self.directory, "annotation.csv"), "a", encoding="utf-8", newline="") as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            while self.str_num == 0:
                writer.writerow([
                    "Absolute path",
                    "Relative path",
                    "Class"
                ])
                self.str_num += 1
            writer.writerow([os.path.join(path, self.directory, class_name, img_name),
                             os.path.join(self.directory, class_name, img_name), class_name])
            self.str_num += 1
