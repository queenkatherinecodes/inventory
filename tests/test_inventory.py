import pytest
from src.inventory import Inventory
from src.product import Product

@pytest.fixture
def empty_inventory():
    return Inventory()

@pytest.fixture
def sample_product():
    return Product("sample", 1, 1)

@pytest.fixture
def stocked_inventory():
    """returns an inventory with some tasty products"""
    inventory = Inventory()
    inventory.add_product(Product("Bamba", 6.0, 2))
    inventory.add_product(Product("Bissli", 5.5, 10))
    return inventory

def test_add_new_product(empty_inventory, sample_product):
    empty_inventory.add_product(sample_product)
    assert len(empty_inventory._products) == 1
    assert empty_inventory.get_product("sample") == sample_product

def test_add_existing_product(empty_inventory):
    blue_bamba = Product("Bamba", 6.0, 1)
    orange_bamba = Product("Bamba", 6.0, 1)
    
    empty_inventory.add_product(blue_bamba)
    empty_inventory.add_product(orange_bamba)
    
    # Should only have one Bamba product
    assert len(empty_inventory._products) == 1
    assert empty_inventory.get_product("Bamba").quantity == 2

def test_remove_product(stocked_inventory):
    stocked_inventory.remove_product("Bamba")
    assert len(stocked_inventory._products) == 1
    assert stocked_inventory.get_product("Bamba") is None

def test_remove_nonexistent_product(empty_inventory):
    with pytest.raises(ValueError):
        empty_inventory.remove_product("Nonexistent")

def test_total_inventory_value(stocked_inventory):
    # 2 Bambas at 6.0 each + 10 Bissli at 5.5 each
    expected_value = (2 * 6.0) + (10 * 5.5)
    assert stocked_inventory.total_inventory_value() == expected_value

def test_get_product(stocked_inventory):
    product = stocked_inventory.get_product("Bissli")
    assert product is not None
    assert product.name == "Bissli"
    assert product.price == 5.5
    assert product.quantity == 10