class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self._author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, pages):
        if not isinstance(pages, int):
            raise TypeError ("Количество страниц должно быть целым")
        if not pages > 0:
            raise ValueError ("Количество страниц должно быть положительным")
        self._pages = pages

    def __repr__(self):
        return f"{super().__repr__()}, pages={self.pages}"

    def __str__(self):
        return f"{super().__str__()}. Количество страниц: {self.pages}"

class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, duration):
        if not isinstance(duration, float):
            raise TypeError("Продолжительность должна быть типа float")
        if not duration > 0:
            raise ValueError("Продолжительность должно быть положительным")
        self._duration = duration

    def __repr__(self):
        return f"{super().__repr__()}, duration={self.duration}"

    def __str__(self):
        return f"{super().__str__()}. Продолжительность: {self.duration}"
