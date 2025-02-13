if __name__ == "__main__":
    class FlyingVehicle:
        """
        Базовый класс для летательных аппаратов.
        :param model: Модель летательного аппарата
        :param max_speed: Максимальная скорость в км/ч

        Пример:
        boeing747 = FlyingVehicle(model="Boeing 747", max_speed=900) # инициализация экземпляра базового класса
        """

        def __init__(self, model: str, max_speed: int) -> None:
            self._model = model # Непубличный атрибут, чтобы предотвратить прямое изменение модели
            self._max_speed = max_speed # Непубличный атрибут, чтобы предотвратить прямое изменение максимальной скорости

        @property
        def model(self) -> str:
            return self._model

        @property
        def max_speed(self) -> int:
            return self._max_speed

        def __str__(self) -> str:
            return f"Летательный аппарат: {self._model}. Максимальная скорость: {self._max_speed}"

        def __repr__(self) -> str:
            return f"{self.__class__.__name__}(model={self._model!r}, max_speed={self._max_speed!r})"

        def take_off(self) -> None:
            """
            Метод поднимает в воздух летательных аппарат
            :return: Новый статус летательного аппарата

            Пример:
            boeing747 = FlyingVehicle(model="Boeing 747", max_speed=900)
            boeing747.take_off()
            """

            print(f"{self._model} взлетает в небо.")

        def land(self) -> None:
            """
            Метод сажает летательный аппарат на землю. Этот метод будет унаследован дочерними классами
            :return: Новый статус летательного аппарата

            Пример:
            boeing747 = FlyingVehicle(model="Boeing 747", max_speed=900)
            boeing747.land()
            """

            print(f" {self._model} совершает посадку.")


    class Airplane(FlyingVehicle):
        """
        Класс самолета, наследующийся от FlyingVehicle.
        :param model: Модель летательного аппарата
        :param max_speed: Максимальная скорость в км/ч
        :param number_of_engines: Количество двигателей

        Пример:
        boeing747 = Airplane(model="Boeing 747", max_speed=900, number_of_engines=4) #инициализируем экземпляр класса
        """

        def __init__(self, model: str, max_speed: int, number_of_engines: int) -> None:
            super().__init__(model, max_speed)
            self._number_of_engines = number_of_engines # Непубличный атрибут, чтобы предотвратить прямое изменение количества

        @property
        def number_of_engines(self) -> int:
            return self._number_of_engines

        @number_of_engines.setter
        def number_of_engines(self, number_of_engines) -> None:
            if not isinstance(number_of_engines, int):
                raise TypeError ("Количество двигателей должно быть целым числом")
            if number_of_engines < 1:
                raise ValueError("Количество двигателей должно быть положительным числом.")
            self._number_of_engines = number_of_engines

        def __repr__(self) -> str:
            return f"{super().__repr__()}, number_of_engines={self.number_of_engines}"

        def __str__(self) -> str:
            return f"{super().__str__()}. Количество двигателей: {self.number_of_engines}"

        def take_off(self) -> None:
            """
            Перегружаем метод в дочернем классе
            :return: Новый статус летательного аппарата с учетом его вида и количества двигателей

            Пример:
            boeing747 = Airplane(model="Boeing 747", max_speed=900, number_of_engines=4)
            boeing747.take_off()
            """
            print(f"Самолет {self.model} начинает взлет с {self.number_of_engines} двигателями.")


    class Helicopter(FlyingVehicle):
        """
        Класс вертолета, наследующийся от FlyingVehicle.
        :param model: Модель летательного аппарата
        :param max_speed: Максимальная скорость в км/ч
        :param rotor_type: Тип ротора вертолета

        Пример:
        apache = Helicopter(model="Apache AH-64", max_speed=300, rotor_type="Main Rotor") #инициализируем экземпляр класса
        """

        def __init__(self, model: str, max_speed: int, rotor_type: str) -> None:
            super().__init__(model, max_speed)
            self._rotor_type = rotor_type # Непубличный атрибут, чтобы предотвратить прямое изменение типа ротора

        @property
        def rotor_type(self) -> str:
            return self._rotor_type

        @rotor_type.setter
        def rotor_type(self, rotor_type) -> None:
            if not isinstance(rotor_type, str):
                raise TypeError ("Тип ротора должен быть типа str")
            if rotor_type == "":
                raise ValueError("Тип ротора не может быть пустым.")
            self._rotor_type = rotor_type

        def __repr__(self) -> str:
            return f"{super().__repr__()}, rotor_type={self.rotor_type}"

        def __str__(self) -> str:
            return f"{super().__str__()}. Количество двигателей: {self.rotor_type}"

        def take_off(self) -> None:
            """
            Перегружаем метод в дочернем классе
            :return: Новый статус летательного аппарата с учетом его вида и типа ротора

            Пример:
            apache = Helicopter(model="Apache AH-64", max_speed=300, rotor_type="Main Rotor")
            apache.take_off()
            """
            print(f"Вертолет {self.model} вертикально взлетает благодаря ротору типа {self.rotor_type}.")
    pass