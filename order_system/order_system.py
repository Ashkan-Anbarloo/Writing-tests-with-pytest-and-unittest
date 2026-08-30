class Product:
    def __init__(self, name, price , stock):
        self.name = name
        self.price = price
        self.stock = stock

    def is_available(self , quantity):
        return self.stock >= quantity

    def reduce_stock(self , quantity):
        if quantity > self.stock:
            raise ValueError("Not enough stock")
        self.stock -= quantity

class OrderItem:
    def __init__(self, product, quantity):
        if quantity <= 0 :
            raise ValueError("Quantity must be greater than 0")
        if not product.is_available(quantity):
            raise ValueError('Insufficient stock for product')

        self.product = product
        self.quantity = quantity

        product.reduce_stock(quantity)

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        item = OrderItem(product, quantity)
        self.items.append(item)

    def total_price(self):
        return sum(item.price for item in self.items)

    def item_count(self):
        return len(self.items)


laptop = Product('Laptop' , price=1000 , stock=5)
mouse = Product('Mouse' , price=50 , stock=10)

my_order = Order()
my_order.add_item(mouse , quantity=3)

print("Total items:" , my_order.item_count())
print("Total price:" , my_order.total_price())

print('Remaining laptop stock' , laptop.stock)
print('Remaining mouse stock' , mouse.stock)