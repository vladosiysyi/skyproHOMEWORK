class Product:
    name: str
    description: str
    quantity: int
    _price: float

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self._price = price  # Приватный атрибут для цены
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт"

    def __add__(self, other):
        if type(self) is not type(other):
            raise TypeError("Сложение возможно только для товаров одного типа")
        return (self.price * self.quantity) + (other.price * other.quantity)

    @property
    def price(self):
        """Геттер для цены."""
        return self._price

    @price.setter
    def price(self, new_price):
        """Сеттер для цены с проверкой на отрицательное значение."""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self._price = new_price

    @classmethod
    def new_product(cls, product_info, product_list):
        """
        Класс-метод для создания нового товара или обновления существующего товара.

        :param product_info: Словарь с информацией о товаре (название, описание, цена, количество)
        :param product_list: Список существующих товаров для поиска дубликатов
        :return: Новый объект класса Product
        """
        name = product_info.get("name")
        description = product_info.get("description")
        price = product_info.get("price")
        quantity = product_info.get("quantity")

        # Проверка наличия товара с таким же названием
        for product in product_list:
            if product.name == name:
                product.quantity += quantity  # Сложение количества
                if product.price < price:
                    product.price = price  # Устанавливаем более высокую цену
                return product

        # Если товара с таким именем нет, создаём новый объект
        new_product = cls(name, description, price, quantity)
        product_list.append(new_product)  # Добавляем новый продукт в список
        return new_product


class Smartphone(Product):
    def __init__(self, name, description, price, quantity, model, efficiency, memory, color):
        super().__init__(name, description, price, quantity)
        self.model = model
        self.efficiency = efficiency
        self.memory = memory
        self.color = color

    def __str__(self):
        return (f"{self.name} ({self.model}), {self.price} руб. Остаток: {self.quantity} шт.\n"
                f"Производительность: {self.efficiency}, Память: {self.memory}GB, Цвет: {self.color}")


class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self):
        return (f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт.\n"
                f"Страна производства: {self.country}, Срок прорастания: {self.germination_period} дней, Цвет: {self.color}")

phone = Smartphone("iPhone", "Смартфон Apple", 100000, 5, "14 Pro", "Высокая", 256, "Черный")
grass = LawnGrass("Green Grass", "Газонная трава", 500, 20, "Голландия", 14, "Зеленый")

prod = Product("Chair", "Comfortable", 100, 2)
print(type(prod))