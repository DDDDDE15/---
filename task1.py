# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
class Car:
    def __init__(self, make: str,model: str, year: int, mileage: float):
        """

        Создание и подготовка к работе объекта "Машина".
        :param make: Марка машины
        :param model: Модель машины
        :param year: Год выпуска машины
        :param mileage: Пробег машины в км

        Примеры:
        >>> car = Car("Chevrolet", "Impala", 1967, 100000) # инициализация экземпляра класса
        """
        if not isinstance(make,str):
            raise TypeError ("Название марки должно быть типы  str")
        self.make = make
        if not isinstance(model, str):
            raise TypeError("Название модели должно быть типа str")
        self.model = model
        if not isinstance(year, int):
            raise TypeError ("Год должен быть типа int")
        if year < 0:
            raise ValueError ("Год не может быть отрицательным числом")
        self.year = year
        if not isinstance(mileage, (int, float)):
            raise TypeError ("Пробег должен быть типа int или float")
        if mileage < 0:
            raise ValueError ("Пробег не может быть отрицательным числом")
        self.mileage = mileage
    def drive_distance(self, distance: float) -> float:
        """

        Функция увеличивает пробег машины на указанную дистанцию.
        :param distance: Пройденная дистанция в километрах
        :raise ValueError: Если количество киллометров отрициательное вызываем ошибку

        :return: Новую величину пробега

        Примеры:
        >>> car = Car("Chevrolet", "Impala", 1967, 100000)
        >>> car.drive_distance(25000)
        """
        ...
    def current_age(self,current_year: int) -> int:
        """

        Функция выдает возраст модели машины.
        :param current_year: Текущий год
        :raise ValueError: Если текущий год меньше года выпуска модели или текущий год отрицательное число вызываем ошибку

        :return: текущий возраст машины

        Примеры:
        >>> car = Car("Chevrolet", "Impala", 1967, 100000)
        >>> car.current_age(2024)
        """
        ...
class House:
    def __init__(self, address: str, rooms: int, square_meters: float):
        """
        Создание и подготовка к работе объекта "Дом".
        :param address: Адрес дома
        :param rooms: Количество комнат в доме
        :param square_meters: Площадь дома в квадратных метрах
        Примеры:
        >>> house = House("улица Ленина дом 1", 5, 150) # инициализация экземпляра класса
        """
        if not isinstance(address, str):
            raise TypeError("Адрес дома должен быть типа str")
        self.address = address
        if not isinstance(rooms, int):
            raise TypeError("Количество комнат должно быть типа int")
        if rooms < 1:
            raise ValueError("Количество комнат должно быть положительным числом")
        self.rooms = rooms
        if not isinstance(square_meters, (float, int)):
            raise TypeError("Площадь дома должна быть типа float или int")
        if square_meters <= 0:
            raise ValueError("Площадь дома должна быть положительным числом")
        self.square_meters = square_meters
    def describe_house(self) -> str:
        """
        Функция возвращает описание дома.
        :return: Строка с описанием дома(адрес, количество комнат, площадь в квадратых метрах)

        Пример:
        >>> house = House("улица Ленина дом 1", 5, 150)
        >>> house.describe_house()
        """
        ...
    def add_room(self, new_rooms: int, new_square: float) -> float:
        """
        Функция добавляет Новые комнаты к дому и пересчитывает его площадь.
        :param new_rooms: Количество новых комнат
        :param new_square: Площадь новых комнат в квадратных метрах
        :raise ValueError: Если количество новых комнат меньше 1
        :raise ValueError: Если площадь новых комнат <= 0

        :return: Новая площадь дома

        Примеры:
        >>> house = House("улица Ленина дом 1", 5, 150)
        >>> house.add_room(2, 30)
        """
        ...
class Lamp:
    def __init__(self, brand: str, wattage: float, color_temperature: int, state: bool):
        """
        Создание и подготовка к работе объекта "Лампочка".
        :param brand: Бренд производителя лампочки
        :param wattage: Мощность лампочки в ваттах
        :param color_temperature: Цветовая температура света в кельвинах
        :param state: Состояние лампочки. True - включена, False - выключена

        Примеры:
        >>> lamp = Lamp("Эра", 11, 4000, False) # инициализация экземпляра класса
        """
        if not isinstance(brand, str):
            raise TypeError ("Бренд должен иметь тип str")
        self.brand = brand
        if not isinstance(wattage, (int, float)):
            raise TypeError ("Мощность должна иметь тип int или float")
        if wattage <= 0:
            raise ValueError ("Мощность должна быть положительной")
        self.wattage = wattage
        if not isinstance(color_temperature, int):
            raise TypeError ("Цветовая температура должна быть типа int")
        if color_temperature < 1:
            raise ValueError ("Цветовая температура должна быть положительной")
        self.color_temperature = color_temperature
        if not isinstance(state, bool):
            raise TypeError ("Состояние лапочки должно быть типа bool")
        self.state = state
    def turn_on_lamp(self) -> bool:
        """
        Функция включает лампочку.
        :return: Новое состояние лампочки

        Пример:
        >>> lamp = Lamp("Эра", 11, 4000, False)
        >>> lamp.turn_on_lamp()
        """
        ...
    def turn_of_lamp(self) -> bool:
        """
        Функция выключает лампочку.
        :return: Новое состояние лампочки

        Пример:
        >>> lamp = Lamp("Эра", 11, 4000, False)
        >>> lamp.turn_of_lamp()
        """
        ...
if __name__ == "__main__":
    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass



