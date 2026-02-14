def is_positive(value: float) -> bool:
    return value > 0

def format_price(value: float)-> str:
    return f"${value:.2f}"

def calculate_discount(price: float, percent: float) -> float:
    discount = price * (percent / 100)
    return price - discount