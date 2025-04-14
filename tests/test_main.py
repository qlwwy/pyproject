import pytest
from src.main import Product, Category

fixture(autouse=True)
def reset_category_counters():
    # Сброс счетчиков перед каждым тестом
    Category.category_count = 0
    Category.product_count = 0

def test_product_initialization():
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5

def test_category_initialization():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category = Category("Смартфоны",  [product1, product2, product3])

    assert category.name == "Смартфоны"
    assert category.description == "Смартфоны"
    assert len(category.products) == 3
    assert Category.category_count == 1
    assert Category.product_count == 3

def test_multiple_categories():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)

    category1 = Category("Смартфоны", [product1, product2, product3])
    category2 = Category("Телевизоры", [product4])

    assert Category.category_count == 2
    assert Category.product_count == 4
