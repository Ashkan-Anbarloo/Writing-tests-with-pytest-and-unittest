def format_price(amount):
    return f'{amount} تومان '

def is_valid_id(value):
    return isinstance(value, int) and value > 0