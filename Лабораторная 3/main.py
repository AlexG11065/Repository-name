class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        print("init basa") # перед сдачей удалить
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):
    """Бумажная книга"""
    def __init__(self, name: str, author: str, pages: int):
        print("init PaperBook ")  # перед сдачей удалить
        super().__init__(name, author)
        if not isinstance(pages, int):
            raise ValueError("Данные должны быть типа int")
        if pages <= 0:
            raise ValueError("Данные не могут быть отрицательными")
        self.pages = pages

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}. Страницы {self.pages}"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        print("init AudioBook ")   # перед сдачей удалить
        super().__init__(name, author)
        if not isinstance(duration, float):
            raise ValueError("Данные должны быть типа float")
        self.duration = duration

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}. Длительность {self.duration}"


if __name__ == "__main__":
    a = Book("Война и Мир", "Л.Н.Толстой")
    b = AudioBook("Война и Мир", "Л.Н.Толстой", 0.99)
    c = PaperBook("Война и Мир", "Л.Н.Толстой", 900)

print(a, b, c, sep="\n")


