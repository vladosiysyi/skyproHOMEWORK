import pytest
from scr.category import Category
from scr.product import Product


@pytest.fixture(autouse=True)
def reset_class_variables():
    """Сбрасываем счётчики перед каждым тестом."""
    Category.total_categories = 0
    Category.total_products = 0


def test_product_initialization():
    """Проверяет правильность инициализации объекта Product."""
    product = Product("Телефон", "Смартфон с камерой", 50000, 10)

    assert product.name == "Телефон"
    assert product.description == "Смартфон с камерой"
    assert product.price == 50000
    assert product.quantity == 10


def test_category_initialization():
    """Проверяет правильность инициализации объекта Category."""
    category = Category("Электроника", "Гаджеты")

    assert category.name == "Электроника"
    assert category.description == "Гаджеты"
    assert category.products == []  # Должен быть пустым списком


def test_category_with_products():
    """Проверяет, что категория корректно хранит товары."""
    product1 = Product("Телефон", "Смартфон", 50000, 10)
    product2 = Product("Ноутбук", "Игровой ноутбук", 100000, 5)

    category = Category("Электроника", "Гаджеты", [product1, product2])

    assert len(category.products) == 2
    assert category.products[0].name == "Телефон"
    assert category.products[1].name == "Ноутбук"


def test_total_categories():
    """Проверяет корректность подсчёта категорий."""
    Category("Электроника", "Гаджеты")
    Category("Одежда", "Разные вещи")

    assert Category.total_categories == 2


def test_total_products():
    """Проверяет корректность подсчёта товаров во всех категориях."""
    product1 = Product("Телефон", "Смартфон", 50000, 10)
    product2 = Product("Ноутбук", "Игровой ноутбук", 100000, 5)

    Category("Электроника", "Гаджеты", [product1, product2])
    Category("Одежда", "Разные вещи")  # Без товаров

    assert Category.total_products == 2
