import pytest

from tests.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def cart():
    return Cart()


class TestProducts:

    def test_product_check_quantity(self, product):
        assert product.check_quantity(1) is True
        assert product.check_quantity(1000) is True
        assert product.check_quantity(1001) is False

    def test_product_buy(self, product):
        product.buy(1)
        assert product.quantity == 999

    def test_product_buy_more_than_available(self, product):
        with pytest.raises(ValueError):
            product.buy(1100)


class TestCart:
    def test_add_product(self, cart, product):
        cart.add_product(product, 1)
        assert cart.products[product] == 1
        cart.add_product(product, 2)
        assert cart.products[product] == 3

    def test_remove_product(self, cart, product):
        cart.add_product(product, 3)
        cart.remove_product(product, 1)
        assert cart.products[product] == 2
        cart.remove_product(product, 2)
        assert product not in cart.products

    def test_remove_product_entirely(self, cart, product):
        cart.add_product(product, 1)
        cart.remove_product(product)
        assert product not in cart.products

    def test_clear(self, cart, product):
        cart.add_product(product, 1)
        cart.clear()
        assert len(cart.products) == 0

    def test_get_total_price(self, cart, product):
        cart.add_product(product, 3)
        assert cart.get_total_price() == 300

    def test_buy(self, cart, product):
        cart.add_product(product, 2)
        cart.buy()
        assert product.quantity == 998
        assert len(cart.products) == 0

    def test_buy_insufficient_stock(self, cart, product):
        cart.add_product(product, 1100)
        with pytest.raises(ValueError):
            cart.buy()
