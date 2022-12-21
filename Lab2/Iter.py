from next_element import next_element


class Iter:
    def __init__(self, path: str):
        """
        param path: path to dir
        """
        self.path = path


    def __next__(self) -> str:
        """
        return: next element
        """
        self.path = next_element(self.path)
        return self.path
