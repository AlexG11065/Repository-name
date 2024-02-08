import doctest


class Car:
    def __init__(self, color: str, weight: int, model: str):
        """
        Конструктор автомобиля
        :param color: цвет
        :param weight: вес
        :param model: модель

        Примеры:
        >>> car1 = Car('red', 1500, 'mazda') # инициализация экземпляра класса
        """
        if not isinstance(color, str):
            raise ValueError('Тип данных цвета должен быть типа str')
        self.color = color

        if not isinstance(weight, (int, float)):
            raise ValueError('Тип данных веса должен быть int')
        self.weight = weight

        if not isinstance(model, str):
            raise ValueError("Тип данных модели должен быть str")
        self.model = model

    def method_1(self, color) -> str:
        """
        Метод фильтрует  машины по цвуту.

        :raise ValueError: Такого цвета нет

        :return: Такой цвет есть

        >>> car1 = Car('red', 1500, 'mazda')
        >>> car1.method_1('red')
        """
        pass

    def method_weight(self, weight: (int, float)):
        """
        Метод фильтрующий машину по весу.
        :raise ValueError: Машина не может весить меньше 1000 кг

        :return: Выводит список имеющихся машин по весу

        >>> car1 = Car('red', 1500, 'mazda')
        >>> car1.method_weight(1500)
        """
        pass

    def method_model(self, model: str):
        """
        :raise: Такой модели нет
        :return: есть

        >>> car1 = Car('red', 1500, 'mazda')
        >>> car1.method_model('mazda')

        """
        pass


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest

    doctest.testmod()