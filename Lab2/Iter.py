from next_element import next_element


class Iterator:
    def __init__(self, path: str):
        self.path = path
        """
        путь к файлу
        """


    def __next__(self) -> str:
        self.path = next_element(self.path)
        return self.path
    """
    возвращает следующий элемент
    """


if __name__ == "__main__":
    Iter = Iterator("C:\\Users\\0\\python_var_7\\dataset\\zebra\\0001.jpg")
    print(Iter.__next__())
