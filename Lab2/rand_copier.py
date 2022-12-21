import os
import random
from copier import create_dir
import shutil
from main import Data


def rand_copier(obj: type(Data), path: str, class_name) -> None:
    """
    :param obj: object Data class
    :param path: new dir for files
    :param class_name: class name
    """
    prev_dir = obj.directory
    create_dir(obj, path)
    allowed_values = list(range(0, 10000))
    for i in range(len(os.listdir(os.path.join(path, prev_dir, class_name)))):
        try:
            n = random.choice(allowed_values)
            shutil.copy(os.path.join(path, prev_dir, class_name, f'{(i + 1):04d}.jpg'),
                        os.path.join(path, obj.directory))
            os.rename(os.path.join(path, obj.directory, f'{(i + 1):04d}.jpg'),
                      os.path.join(path, obj.directory, f'{n:05d}.jpg'))
            obj.adder(path, class_name, f'{n:05d}.jpg')
            allowed_values.remove(n)
        except OSError:
            print("Some error")
