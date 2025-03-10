from scr.product import Product


class Category:
    name: str
    description: str
    __products: list

    # Атрибуты класса для подсчета категорий и продуктов
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []
        # Увеличиваем счетчики атрибутов класса
        Category.category_count += 1
        Category.product_count += len(self.__products)  # Используем self.__products вместо products

    def __str__(self):
        """Возвращает строку с информацией о категории и общем количестве товаров."""
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{
            self.name}, количество продуктов: {
            len(
                self.__products)} шт., общее количество товаров на складе: {total_quantity} шт."

    def middle_price(self):
        """Возвращает среднюю цену товаров в категории."""
        try:
            total_price = sum(product.price for product in self.__products)
            total_products = len(self.__products)
            return total_price / total_products
        except ZeroDivisionError:
            return 0  # Если в категории нет товаров, возвращаем 0

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product или его наследников")
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        if not self.__products:
            return "список пуст"
        return "".join(f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт.\n" for p in self.__products)
