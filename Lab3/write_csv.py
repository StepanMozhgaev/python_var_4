import csv
import os


def write_csv(directory_obj: str, file: str, name: str) -> None:
    """Writes the absolute and relative path of the image to csv, return NONE.
    Args:
        directory_obj (str): full path to the folder.
        file (str): the path to the file to save.
        name (str): object class.
    """
    file = os.path.join(file, "annotation.csv")
    with open(file, "a", encoding="utf-8", newline="") as f:
        f_writer = csv.DictWriter(f, fieldnames=["Absolut_path", "Relative_patch", "Class"], delimiter="|")
        data = os.listdir(directory_obj)
        r_directory_obj = "dataset"
        for i in data:
            f_writer.writerow({"Absolut_path": os.path.join(directory_obj, i),
                               "Relative_patch": os.path.join(r_directory_obj, f"{name}_{i}"), "Class": name})


def main() -> None:
    directory_zebra = "C:\\Users\\0\\python_var_7\\dataset\\zebra"
    directory_bay_horse = "C:\\Users\\0\\python_var_7\\dataset\\bay_horse"
    file = "C:\\Users\\0\\python_var_7\\"

    write_csv(directory_zebra, file, "zebra")
    write_csv(directory_bay_horse, file, "bay horse")


if __name__ == "__main__":
    main()
