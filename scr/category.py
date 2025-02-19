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

    def add_product(self, product):
        """добавление продукта в категорию"""
        self.__products.append(product)
        Category.category_count += 1

    @property
    def products(self):
        if not self.__products:
            return "список пуст"
        return "".join(f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт.\n" for p in self.__products)
