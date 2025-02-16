class Category:
    name: str
    description: str
    products: list

    # Атрибуты класса для подсчета категорий и продуктов
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.products = products if products else []

        # Увеличиваем счетчики атрибутов класса
        Category.category_count += 1
        Category.product_count += len(products)  # Добавляем количество продуктов из этого списка
