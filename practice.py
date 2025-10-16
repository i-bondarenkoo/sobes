from enum import Enum


class Product:
    def __init__(self, name: str, price: int, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def set_new_quantity(self, pay_quantity: int):
        if self.quantity - pay_quantity >= 0:
            self.quantity -= pay_quantity
        else:
            # return f"Товара в количестве {pay_quantity} в данный момент нет на складе"
            raise ValueError(
                "Товара в количестве {pay_quantity} в данный момент нет на складе"
            )
        return True

    def __str__(self):
        return f"Продукт - {self.name}, цена за единицу - {self.price}, общее количество на складе - {self.quantity}"

    def __repr__(self):
        return f"Product(name={self.name}, цена товара={self.price}руб, общее количество на складе={self.quantity})"


class Customer:
    def __init__(self, name: str, email: str, balance: int):
        self.name = name
        self.email = email
        self.balance = balance

    def __str__(self):
        return f"Покупатель - {self.name}, адрес почтового ящика - {self.email}, количество денег для покупки - {self.balance}"

    def __repr__(self):
        return f"Customer(name={self.name}, email={self.email}, balance={self.balance})"


class OrderStatus(str, Enum):
    paid = "paid"
    canceled = "canceled"
    packed = "packed"
    created = "created"


class Order:
    def __init__(
        self,
        customer: Customer,
        status: OrderStatus = "created",
    ):
        self.product_list: list[tuple[Product, int]] = []
        self.price_at_order = 0
        self.status = status
        self.customer = customer

    def add_product(self, product: Product, pay_quantity: int):
        if isinstance(product, Product) and pay_quantity > 0:
            pair: tuple = (product, pay_quantity)
            self.product_list.append(pair)
            self.price_at_order += pay_quantity * product.price
        return "Продукт добавлен в заказ"

    def set_customer(self, new_customer: Customer):
        if isinstance(new_customer, Customer):
            self.customer = new_customer
        else:
            raise ValueError("Переданные объект не относится к классу покупателя")

    def get_total_price(self):
        return f"Общая стоимость заказа - {self.price_at_order}"

    def pay_order(self):
        
    def __str__(self):
        list_to_str = "\n".join(str(element) for element in self.product_list)
        return f"Список товаров в заказе - [{list_to_str}], статус заказа - {self.status}, стоимость заказа - {self.price_at_order}, покупатель - {self.customer.name}"


potato = Product("Картофель", 30, 7)
# print(potato)

nikita = Customer("Никита", "nikita@mail.ru", 1500)
# print(nikita)

order1 = Order(nikita)
# print(order1)
order1.add_product(potato, 4)
print("Заказ пользователя ---", order1)
order1.pay_order(product=potato, customer=nikita, pay_quantity=4)
print("Заказ был оплачен ---", order1)
print("Данные покупателя --- ", nikita)
print("Данные о товаре ---", potato)
