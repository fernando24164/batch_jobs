import csv
import datetime
from pathlib import Path
from random import randint

PATH = str(Path.cwd())

GENERATED_VALUES = 200

headers_cart_update = [
    "page_type",
    "url",
    "amount",
    "amount_previous",
    "datetime",
    "logged_user",
    "event",
    "product_id",
]


with open(f"{PATH}/src/data/data_cart_update.csv", "w", encoding="utf8") as csv_file:
    writer = csv.writer(csv_file, delimiter=",")
    writer.writerow(headers_cart_update)

    page_types = ["contact", "home", "sellers"]
    urls = ["cool-shop.com", "nice-store.com", "amazing-webpage.com"]
    products_id = [
        1233,
        4343,
        5465,
        43213,
        1234,
    ]

    for i in range(GENERATED_VALUES):
        amount = randint(0, 25)
        amount_previous = amount - randint(0, amount)
        logged_user = bool(randint(0, 1))

        writer.writerow(
            [
                page_types[randint(0, 2)],
                urls[randint(0, 2)],
                amount,
                amount_previous,
                datetime.datetime.today() - datetime.timedelta(days=randint(0, 7)),
                logged_user,
                "cart_update",
                products_id[randint(0, len(products_id) - 1)],
            ]
        )

headers_user_visit = [
    "page_type",
    "url",
    "datetime",
    "logged_user",
    "event",
    "product_id",
    "user_id",
]

with open(f"{PATH}/src/data/data_user_visit.csv", "w", encoding="utf8") as csv_file:
    writer = csv.writer(csv_file, delimiter=",")
    writer.writerow(headers_user_visit)

    page_types = ["contact", "home", "sellers"]
    urls = ["cool-shop.com", "nice-store.com", "amazing-webpage.com"]
    products_id = [
        1233,
        4343,
        5465,
        43213,
        1234,
    ]
    user_ids = [
        11,
        22,
        33,
        44,
        55,
        66,
        77,
        88,
        99,
    ]

    for i in range(GENERATED_VALUES):
        writer.writerow(
            [
                page_types[randint(0, 2)],
                urls[randint(0, 2)],
                datetime.datetime.today() - datetime.timedelta(days=randint(0, 7)),
                bool(randint(0, 1)),
                "user_visit",
                products_id[randint(0, len(products_id) - 1)],
                user_ids[randint(0, len(user_ids) - 1)] if logged_user else None,
            ]
        )
