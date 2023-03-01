import csv
import os
import shutil
import tqdm


def copy_dataset(directory_obj: str, c_directory_obj: str, name: str) -> None:
    """Copies all files from one folder to another, return NONE.
    Args:
        directory_obj (str): the path of the source folder.
        c_directory_obj (str): folder path to copy.
        name (str): object class.
    """
    c_directory_obj1 = os.path.join(c_directory_obj, "dataset_2")
    if not os.path.isdir(c_directory_obj1):
        os.makedirs(c_directory_obj1)

    data = os.listdir(directory_obj)
    for i in tqdm.tqdm(data):
        shutil.copy(os.path.join(directory_obj, i), os.path.join(c_directory_obj1, f"{name}_{i}"))

    write_csv_copy(directory_obj, c_directory_obj1, name)


def write_csv_copy(directory_obj: str, c_directory_obj: str, name: str) -> None:
    """Writes the absolute and relative path of the image to csv, return NONE.
    Args:
        directory_obj (str): the path of the source folder.
        c_directory_obj (str): folder path to copy.
        name (str): object class.
    """
    data = os.listdir(directory_obj)
    r_directory_obj = "dataset_2"

    file = os.path.join(c_directory_obj, "copy.csv")
    with open(file, "a", encoding="utf-8", newline="") as f:
        f_writer = csv.DictWriter(f, fieldnames=["Absolut_path", "Relative_patch", "Class"], delimiter="|")
        for i in data:
            f_writer.writerow({"Absolut_path": os.path.join(c_directory_obj, f"{name}_{i}"),
                               "Relative_patch": os.path.join(r_directory_obj, f"{name}_{i}"), "Class": name})


def main() -> None:
    c_directory = "C:\\Users\\0\\python_var_7\\dataset\\new_dataset_3"
    directory_zebra = "C:\\Users\\0\\python_var_7\\dataset\\zebra"
    directory_bay_horse = "C:\\Users\\0\\python_var_7\\dataset\\bay_horse"

    copy_dataset(directory_zebra, c_directory, "zebra")
    copy_dataset(directory_bay_horse, c_directory, "bay horse")


if __name__ == "__main__":
    main()
