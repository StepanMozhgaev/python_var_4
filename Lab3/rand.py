import csv
import os
import shutil
import tqdm
import random


def copy_dataset(directory_obj: str, c_directory_obj: str, name: str) -> None:
    """Copies all files from one folder to another, return NONE.
    Args:
        directory_obj (str): the path of the source folder.
        c_directory_obj (str): folder path to copy.
        name (str): object class.
    """
    c_directory_obj1 = os.path.join(c_directory_obj, "dataset_3")
    if not os.path.isdir(c_directory_obj1):
        os.makedirs(c_directory_obj1)

    r_list = list(range(1, 10001))
    random.shuffle(r_list)
    r_list = [str(i) for i in r_list]

    c_data = os.listdir(c_directory_obj1)
    if c_data:
        c_data = list(map(lambda sub: int(''.join([ele for ele in sub if ele.isnumeric()])), c_data))
        c_data = [str(i) for i in c_data]
        for i in c_data:
            r_list.remove(i)

    j = 0
    copy_list = []
    data = os.listdir(directory_obj)
    for i in tqdm.tqdm(data):
        so = str(r_list[j])
        copy_list.append(so)
        shutil.copy(os.path.join(directory_obj, i), os.path.join(c_directory_obj1, f"{so}.jpeg"))
        j += 1

    write_csv_copy(c_directory_obj1, name, copy_list)


def write_csv_copy(c_directory_obj: str, name: str, copy_list: list) -> None:
    """Writes the absolute and relative path of the image to csv, return NONE.
    Args:
        c_directory_obj (str): folder path to copy.
        name (str): object class.
        copy_list (list): numbers of copied objects.
    """
    file = os.path.join(c_directory_obj, "rand.csv")
    with open(file, "a", encoding="utf-8", newline="") as f:
        f_writer = csv.DictWriter(f, fieldnames=["Absolut_path", "Relative_patch", "Class"], delimiter="|")
        r_directory_obj = "dataset_3"
        for i in copy_list:
            f_writer.writerow(
                {"Absolut_path": os.path.join(c_directory_obj, i),
                 "Relative_patch": os.path.join(r_directory_obj, i), "Class": name})


def main() -> None:
    c_directory = "C:\\Users\\0\\python_var_7\\dataset\\new_dataset_2"
    directory_zebra = "C:\\Users\\0\\python_var_7\\dataset\\zebra"
    directory_bay_horse = "C:\\Users\\0\\python_var_7\\dataset\\bay_horse"

    copy_dataset(directory_zebra, c_directory, "zebra")
    copy_dataset(directory_bay_horse, c_directory, "bay horse")


if __name__ == "__main__":
    main()
