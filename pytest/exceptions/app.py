def divide(a,b):
    return a/b


class InvalidAgeError(Exception):
    pass

def register_user(age):
    if age<0:
        raise InvalidAgeError('سن نمیتواند منفی باشد')
    return f"age {age} is ok"