class Divider:
    def divide(self, a, b):
        if not isinstance (a,(int,float)) or not isinstance (b,(int,float)):
            raise TypeError('Divider can only divide integers or floats')

        if b == 0:
            raise ZeroDivisionError('Divider can not be zero')

        return a / b