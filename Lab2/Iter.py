from next_element import next_element


class Iterator:
    def __init__(self, path: str):
        self.path = path

    def __next__(self) -> str:
        self.path = next_element(self.path)
        return self.path


if __name__ == "__main__":
    iter = Iterator("C:\\Users\\0\\python_var_7\\dataset\\zebra\\0001.jpg")
    print(iter.__next__())
