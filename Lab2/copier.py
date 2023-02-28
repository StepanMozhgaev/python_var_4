import os
import shutil
from Data import Data


def create_dir(obj: type(Data), path: str) -> None:
    """
    :param obj: object Data class
    :param path: new dir path
    """
    try:
        os.mkdir(os.path.join(path, "new_dataset"))
        obj.directory = "new_dataset"
    except OSError as err:
        print(err)


def replace_dir(obj: type(Data), path: str, class_name) -> None:
    """
    :param obj: object Data class
    :param path: new dir path
    :param class_name: class name
    """
    prev_dir = obj.directory
    create_dir(obj, path)
    for i in range(len(os.listdir(os.path.join(path, prev_dir, class_name)))):
        try:
            shutil.copy(os.path.join(path, prev_dir, class_name, f'{(i+1):04d}.jpg'), os.path.join(path, obj.directory))
            os.rename(os.path.join(path, obj.directory, f'{(i+1):04d}.jpg'),
                      os.path.join(path, obj.directory, f'{class_name}_{(i+1):04d}.jpg'))
            obj.adder(path, class_name, f'{class_name}_{(i+1):04d}.jpg')
        except OSError as err:
            print(err)


if __name__ == "__main__":
    obj = Data("C:\\Users\\0\\python_var_7\\dataset\\")
    replace_dir(obj, "C:\\Users\\0\\python_var_7\\dataset\\", "zebra")
    replace_dir(obj, "C:\\Users\\0\\python_var_7\\dataset\\", "bay horse")
