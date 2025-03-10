import pytest
from scr.category import Category
from scr.product import Product, Smartphone, LawnGrass


@pytest.fixture
def sample_products():
    return [
        Product("Laptop", "Powerful laptop", 1000, 5),
        Product("Phone", "Smartphone with great camera", 500, 10),
    ]


@pytest.fixture
def sample_category(sample_products):
    return Category("Electronics", "Devices and gadgets", sample_products)


@pytest.fixture
def empty_category():
    return Category("Empty", "No products")


def test_category_creation(sample_category):
    assert sample_category.name == "Electronics"
    assert sample_category.description == "Devices and gadgets"
    assert len(sample_category.products) > 0


def test_category_str(sample_category):
    assert str(sample_category) == "Electronics, количество продуктов: 2 шт., общее количество товаров на складе: 15 шт."


def test_empty_category(empty_category):
    assert empty_category.products == "список пуст"


def test_add_product(sample_category):
    new_product = Product("Tablet", "Portable device", 300, 7)
    initial_count = Category.product_count
    sample_category.add_product(new_product)
    assert "Tablet" in sample_category.products
    assert Category.product_count == initial_count + 1  # Проверяем, что счетчик увеличился


def test_add_invalid_product(sample_category):
    with pytest.raises(TypeError):
        sample_category.add_product("Not a product")


def test_product_creation():
    product = Product("Headphones", "Noise cancelling", 200, 15)
    assert product.name == "Headphones"
    assert product.description == "Noise cancelling"
    assert product.price == 200
    assert product.quantity == 15


def test_product_str():
    product = Product("Monitor", "4K Display", 400, 8)
    assert str(product) == "Monitor, 400 руб. Остаток: 8 шт"


def test_product_price_setter():
    product = Product("Monitor", "4K Display", 400, 8)
    product.price = 450
    assert product.price == 450
    product.price = -100  # Должен остаться 450
    assert product.price == 450


def test_product_addition():
    product1 = Product("Chair", "Comfortable", 100, 2)
    product2 = Product("Chair", "Comfortable", 300, 1)
    phone = Smartphone("iPhone", "Смартфон Apple", 100000, 5, "14 Pro", "Высокая", 256, "Черный")
    grass = LawnGrass("Green Grass", "Газонная трава", 500, 20, "Голландия", 14, "Зеленый")
    assert product1 + product2 == 500  # 100*2 + 300*1
    with pytest.raises(TypeError):
        phone + grass


def test_new_product_creation():
    product_list = []
    product_info = {"name": "Mouse", "description": "Wireless mouse", "price": 50, "quantity": 20}
    new_product = Product.new_product(product_info, product_list)
    assert new_product in product_list
    assert new_product.name == "Mouse"


def test_new_product_update():
    product_list = [Product("Keyboard", "Mechanical keyboard", 80, 5)]
    product_info = {"name": "Keyboard", "description": "Mechanical keyboard", "price": 90, "quantity": 3}
    updated_product = Product.new_product(product_info, product_list)
    assert updated_product.quantity == 8
    assert updated_product.price == 90


def test_product_price_validation():
    product = Product("Speaker", "Bluetooth speaker", 150, 6)
    product.price = -50  # Попытка установить отрицательную цену
    assert product.price == 150  # Цена не изменилась


def test_smartphone_str():
    smartphone = Smartphone(
        name="iPhone",
        description="Apple smartphone",
        price=100000,
        quantity=5,
        model="14 Pro",
        efficiency="High",
        memory=256,
        color="Black"
    )
    expected_str = (
        "iPhone (14 Pro), 100000 руб. Остаток: 5 шт.\n"
        "Производительность: High, Память: 256GB, Цвет: Black"
    )
    assert str(smartphone) == expected_str


def test_lawn_grass_str():
    lawn_grass = LawnGrass(
        name="Green Grass",
        description="Газонная трава",
        price=500,
        quantity=20,
        country="Голландия",
        germination_period=14,
        color="Зеленый"
    )
    expected_str = (
        "Green Grass, 500 руб. Остаток: 20 шт.\n"
        "Страна производства: Голландия, Срок прорастания: 14 дней, Цвет: Зеленый"
    )
    assert str(lawn_grass) == expected_str


def test_classinfo_repr():
    phone = Smartphone("iPhone", "Apple smartphone", 100000, 5, "14 Pro", "High", 256, "Black")
    grass = LawnGrass("Green Grass", "Газонная трава", 500, 20, "Голландия", 14, "Зеленый")
    assert repr(phone) == "Smartphone(iPhone, Apple smartphone, 100000,5)"
    assert repr(grass) == "LawnGrass(Green Grass, Газонная трава, 500,20)"


def test_create_product_with_zero_quantity():
    """Тест: создание товара с нулевым количеством должно вызвать ValueError."""
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Product("Test Product", "Some description", 100, 0)
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Smartphone("iPhone", "Apple smartphone", 100000, 0, "14 Pro", "High", 256, "Black")
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        LawnGrass("Green Grass", "Газонная трава", 500, 0, "Голландия", 14, "Зеленый")


def test_middle_price_with_products():
    """Тест: расчет средней цены товаров, если в категории есть товары."""
    product1 = Product("iPhone", "Смартфон", 100000, 5)
    product2 = Product("MacBook", "Ноутбук", 150000, 2)

    category = Category("Электроника", "Гаджеты", [product1, product2])

    expected_avg_price = (100000 + 150000) / 2  # Среднее арифметическое
    assert category.middle_price() == expected_avg_price


def test_middle_price_no_products():
    """Тест: средняя цена в пустой категории должна быть 0 (деление на ноль не должно происходить)."""
    category = Category("Одежда", "Категория без товаров")
    assert category.middle_price() == 0
