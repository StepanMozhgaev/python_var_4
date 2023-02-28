from next_element import next_element


class Iterator:
    def __init__(self, path: str):
        """
        :param path: path to file
        """
        self.path = path

    def __next__(self) -> str:
        """
        :return: next element
        """
        self.path = next_element(self.path)
        return self.path


if __name__ == "__main__":
    Iterator_1 = Iterator("C:\\Users\\0\\python_var_7\\dataset\\zebra\\0001.jpg")
    print(Iterator_1.__next__())
