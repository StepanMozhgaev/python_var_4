from next_element import next_element


class Iter:
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

