import pytest
from scr.category import Category
from scr.product import Product


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


def test_empty_category(empty_category):
    assert empty_category.products == "список пуст"


def test_add_product(sample_category):
    new_product = Product("Tablet", "Portable device", 300, 7)
    sample_category.add_product(new_product)
    assert "Tablet" in sample_category.products


def test_product_creation():
    product = Product("Headphones", "Noise cancelling", 200, 15)
    assert product.name == "Headphones"
    assert product.description == "Noise cancelling"
    assert product.price == 200
    assert product.quantity == 15


def test_product_price_setter():
    product = Product("Monitor", "4K Display", 400, 8)
    product.price = 450
    assert product.price == 450
    product.price = -100  # Должен остаться 450
    assert product.price == 450


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
