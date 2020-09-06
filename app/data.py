import csv
import requests


def get_data():
    RESULT = {}
    with open('/app/data/aapl.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        # Date,Volume,Close,Average
        for row in reader:
            for column, value in row.items():
                RESULT.setdefault(column, []).append(value)
    return RESULT


def get_apple_stock_price():
    data = get_data()
    metadata = { "type": "A",
                 "style": "border:1px solid green; "}
    data["metadata"] = metadata
    return data


def get_amazon_stock_price():
    data = get_data()
    metadata = { "type": "B",
                 "style": "border:2px solid red; "}
    data["metadata"] = metadata
    return data
