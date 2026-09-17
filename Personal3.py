#3rd personal Project
class Plane:
    def __init__(self, model, passenger_count, max_speed, range):
        self.model = model
        self.passenger_count = passenger_count
        self.max_speed = max_speed
        self.range = range
        self.stock = Stock()
        self.in_stock = True
        self.price = Price()

    def print_plane_info(self):
        print(f"Model: {self.model}")
        print(f"Passenger Count: {self.passenger_count}")
        print(f"Max Speed: {self.max_speed} km/h")
        print(f"Range: {self.range} km")
        print(f"In Stock: {self.stock.stock}")
        print(f"Price: ${self.price.price}")

class Stock:
    def __init__(self, stock=1):
        self.stock = stock

    def add_plane(self, plane, to_add):
        plane.stock.stock += to_add

    def buy(self, plane, to_buy):
        if plane.stock >= to_buy:
            plane.stock -= to_buy
            return f"{to_buy} {plane.model} planes purchased successfully"
        else:
            return "Not enough stock available"

    def in_stock(self, plane):
        if plane.stock == 0:
            plane.in_stock = False

class Price:
    def __init__(self, price=100000):
        self.price = price

    def set_price(self, new_price):
        self.price = new_price

    def discount(self, discount_percent):
        self.price -= (self.price * discount_percent / 100)

    def inflate(self, inflate_percent):
        self.price += (self.price * inflate_percent / 100)

p1 = Plane("Boeing 747", 416, 614, 8000)
p1.price.set_price(130000000)
p1.stock.add_plane(p1, 5)
p1.print_plane_info()