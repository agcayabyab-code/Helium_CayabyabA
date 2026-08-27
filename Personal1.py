#Car shop program(only for testing my classes knowledge)
class Car:
    def __init__(self, brand, model, year):
        self.year = year
        self.brand = brand
        self.model = model
        self.price = Price()
        self.qty = Quantity()

    def print_car_info(self):
        print(self.year, self.brand, self.model)
        print(f"Quantity: {self.qty.quantity}")
        print(f"Price: {self.price.price}")
        print()

class Price:
    def __init__(self, price=10):
        self.price = price

    def set_price(self, new_price):
        self.price = new_price

class Quantity:
    def __init__(self, quantity=1):
        self.quantity = quantity

    def add_car(self, car, quantity):
        car.qty.quantity += quantity


    def buy(self,car, to_buy):
        if car.qty.quantity >= to_buy:
            car.qty.quantity -= to_buy
            return True
        else:
            return None
        
class Shop:
    def __init__(self, name):
        self.cars = []
        self.name = name
    def add_cars(self, car):
        self.cars.append(car) 
    def print_cars(self):
        for car in self.cars:
            print(car.year, car.brand, car.model)
            print(f"Quantity: {car.qty.quantity}")
            print(f"Price: {car.price.price}")
            print()

    def print_total_price(self):
        total_price = 0
        for car in self.cars:
            total_price += car.price.price*car.qty.quantity

        print(f"Total price: {total_price}")
#Demonstration of buying, restocking, and displaying cars in the shop
s = Shop("Andy Car Shop")
c1 = Car("Mitsubishi", "Lancer Evolution", "2002")
c1.qty.add_car(c1, 3)
s.add_cars(c1)
c1.price.set_price(2)
c1.qty.buy(c1, 1)

c2 = Car("Toyota", "Supra Mk-4", "1994")
c2.qty.add_car(c2, 12)
c2. n.set_price(250)
s.add_cars(c2)

c3 = Car("Isuzu", "D-Max", "2025")
c3.qty.add_car(c3, 20)
c3.price.set_price(52)
s.add_cars(c3)

c4 = Car("Mitsubishi", "Montero Sport", "2010")
c4.qty.add_car(c4, 10)
c4.price.set_price(100)
c4.qty.buy(c4, 1)
s.add_cars(c4)

c5 = Car("Mitsubishi", "Xpander", "2022")
c5.qty.add_car(c5, 15)
c5.price.set_price(125)
s.add_cars(c5)
s.print_cars()
s.print_total_price()

print()
c5.qty.buy(c5, 14)
s.print_cars()
s.print_total_price()