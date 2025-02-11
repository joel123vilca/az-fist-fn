import datetime

def get_all_products():
    return [
        {"id": 1, "name": "Milk", "expiry_date": "2025-02-05"},
        {"id": 2, "name": "Cheese", "expiry_date": "2025-01-25"},
        {"id": 3, "name": "Bread", "expiry_date": "2025-02-01"},
        {"id": 4, "name": "Yogurt", "expiry_date": datetime.datetime.utcnow().strftime("%Y-%m-%d")}
    ]