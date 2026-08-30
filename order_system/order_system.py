class Product:
    """مدل محصول - شامل نام، قیمت و موجودی انبار است."""
    def __init__(self, name, price, stock):
        self.name = name                # نام محصول
        self.price = price              # قیمت هر واحد از محصول
        self.stock = stock              # تعداد موجودی در انبار

    def is_available(self, quantity):
        """
        بررسی اینکه آیا تعداد مورد نیاز از محصول در انبار موجود است یا نه.
        اگر موجودی بیشتر یا مساوی با تعداد درخواستی باشد، True برمی‌گرداند.
        """
        return self.stock >= quantity

    def reduce_stock(self, quantity):
        """
        کاهش موجودی محصول پس از سفارش.
        اگر تعداد درخواستی بیشتر از موجودی باشد، خطا می‌دهد.
        """
        if quantity > self.stock:
            raise ValueError("Not enough stock available")
        self.stock -= quantity  # کاهش موجودی

class OrderItem:
    """مدل آیتم سفارش - نشان‌دهنده یک محصول خاص با تعداد مشخص در سفارش است."""
    def __init__(self, product, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero")  # تعداد نمی‌تواند منفی یا صفر باشد
        if not product.is_available(quantity):
            raise ValueError("Insufficient stock for product")  # بررسی موجودی

        self.product = product
        self.quantity = quantity
        self.price = product.price * quantity  # محاسبه قیمت کل این آیتم

        product.reduce_stock(quantity)  # کاهش موجودی محصول پس از سفارش

class Order:
    """مدل سفارش کلی - شامل چند آیتم است."""
    def __init__(self):
        self.items = []  # لیست آیتم‌های سفارش

    def add_item(self, product, quantity):
        """
        افزودن یک محصول خاص به سفارش.
        ابتدا آیتم را می‌سازد و سپس به لیست سفارش اضافه می‌کند.
        """
        item = OrderItem(product, quantity)
        self.items.append(item)

    def total_price(self):
        """
        محاسبه مجموع قیمت تمام آیتم‌های سفارش.
        """
        return sum(item.price for item in self.items)

    def item_count(self):
        """
        تعداد کل آیتم‌های مختلف موجود در سفارش را برمی‌گرداند.
        """
        return len(self.items)


# ساخت محصولات
laptop = Product("Laptop", 1000, 5)
mouse = Product("Mouse", 50, 10)

# ایجاد سفارش جدید
my_order = Order()

# افزودن آیتم‌ها
my_order.add_item(laptop, 2)  # خرید ۲ عدد لپ‌تاپ
my_order.add_item(mouse, 3)   # خرید ۳ عدد موس

# بررسی اطلاعات سفارش
print("Total items:", my_order.item_count())     # خروجی: 2
print("Total price:", my_order.total_price())    # خروجی: 2150

# بررسی موجودی جدید
print("Remaining laptop stock:", laptop.stock)   # خروجی: 3
print("Remaining mouse stock:", mouse.stock)     # خروجی: 7
