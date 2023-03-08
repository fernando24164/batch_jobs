import pytest
import pandas as pd


@pytest.fixture
def cart_updates():
    return pd.read_csv("./fixtures/cart_update.csv")
