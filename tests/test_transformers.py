import pytest

from src.transformers.example_transformer import get_expensive_cart_update


def test_get_expensive_cart_update(cart_updates):
    transform = get_expensive_cart_update(cart_updates)
    assert len(transform)
