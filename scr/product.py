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
