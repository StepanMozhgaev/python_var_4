import os
import shutil
from main import Data


def create_dir(obj: type(Data), path: str) -> None:
    """
    :param obj: object Data class
    :param path: path to new dir
    """
    try:
        os.mkdir(os.path.join(path, "new_dataset"))
        obj.directory = "new_dataset"
    except OSError:
        shutil.rmtree(os.path.join(path, "new_dataset"))
        os.mkdir(os.path.join(path, "new_dataset"))
        obj.directory = "new_dataset"


def replace_dir(obj: type(Data), path: str, class_name) -> None:
    """
    :param obj: object Data class
    :param path: path to new dir
    :param class_name: class name(zebra/bay horse)
    """
    prev_dir = obj.directory
    create_dir(obj, path)
    for i in range(len(os.listdir(os.path.join(path, prev_dir, class_name)))):
        try:
            shutil.copy(os.path.join(path, prev_dir, class_name, f'{(i+1):04d}.jpg'), os.path.join(path, obj.directory))
            os.rename(os.path.join(path, obj.directory, f'{(i+1):04d}.jpg'),
                      os.path.join(path, obj.directory, f'{class_name}_{(i+1):04d}.jpg'))
            obj.adder(path, class_name, f'{class_name}_{(i+1):04d}.jpg')
        except OSError:
            print("No files found")
