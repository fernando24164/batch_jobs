import pandas as pd


def get_expensive_cart_update(df: pd.DataFrame):
    return df[df["amount"] >= 8]


def get_logged_users(df: pd.DataFrame):
    return df[df["logged_user"]]


def run_transformations(data: pd.DataFrame):
    return data.pipe(get_expensive_cart_update).pipe(get_logged_users)


# Class based solution
class Transformer:
    def __init__(self, data_loaded: pd.DataFrame) -> None:
        self.data = data_loaded

    def get_expensive_cart_update(self) -> None:
        self.data = self.data[self.data["amount"] >= 8]
        return self

    def get_logged_users(self) -> None:
        self.data = self.data[self.data["logged_user"]]
        return self

    def run_transformations(self) -> pd.DataFrame:
        self.get_expensive_cart_update().get_logged_users()
        return self.data
