import datetime
from random import random
class Airport:
    def __init__(self, name, code, city):
        self.name = name
        self.code = code
        self.city = city
        self.max_plane_capacity = 50
        self.current_plane_count = 0

    def get_info(self):
        return f"{self.name} ({self.code}) - {self.city}"

class Flight:
    def __init__(self, flight_number, origin, destination, departure_time, arrival_time, airline):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.airline = airline

    def get_flight_info(self):
        return f"{self.airline} Flight {self.flight_number}: {self.origin.get_info()} to {self.destination.get_info()} - Departure: {self.departure_time}, Arrival: {self.arrival_time}"

    def calculate_duration(self):
        departure = datetime.strptime(self.departure_time, "%Y-%m-%d %H:%M")
        arrival = datetime.strptime(self.arrival_time, "%Y-%m-%d %H:%M")
        duration = arrival - departure
        return duration

    def take_off(self):
        self.origin.current_plane_count -= 1
        print(f"{self.airline} Flight {self.flight_number} has taken off from {self.origin.get_info()}, bound for {self.destination.get_info()}.")

    def land(self):
        if self.destination.current_plane_count < self.destination.max_plane_capacity:
            self.destination.current_plane_count += 1
            print(f"{self.airline} Flight {self.flight_number} has landed at {self.destination.get_info()}.")
        else:
            print(f"{self.airline} Flight {self.flight_number} cannot land. {self.destination.get_info()} has reached its maximum plane capacity.")

    def crash(self):
        print(f"{self.airline} Flight {self.flight_number} has crashed. Emergency services have been notified.")

    def go_around(self):
        print(f"{self.airline} Flight {self.flight_number} is going around. The flight will attempt to land again.")

    def divert(self, new_destination):
        print(f"{self.airline} Flight {self.flight_number} is diverting to {new_destination.get_info()}.")
        self.destination = new_destination

    def failure(self):
        chance_of_failure = 10  # 10% chance of failure
        if random.randint(1, 100) <= chance_of_failure:
            print(f"{self.airline} Flight {self.flight_number} has experienced a failure. The flight will return to {self.origin.get_info()}.")
            self.destination = self.origin

naia = Airport("Ninoy Aquino International Airport", "MNL", "Manila")
mactan = Airport("Mactan-Cebu International Airport", "CEB", "Cebu City")
jfk = Airport("John F. Kennedy International Airport", "JFK", "New York City")
lax = Airport("Los Angeles International Airport", "LAX", "Los Angeles")
ohare = Airport("O'Hare International Airport", "ORD", "Chicago")
haneda = Airport("Haneda Airport", "HND", "Tokyo")
narita = Airport("Narita International Airport", "NRT", "Tokyo")
kansai = Airport("Kansai International Airport", "KIX", "Osaka")
kai_tak = Airport("Kai Tak Airport", "HKG", "Hong Kong")

pal125 = Flight("PR125", naia, mactan, "2024-06-15 08:00", "2024-06-15 09:30", "Philippine Airlines")

pal125.take_off()
print(pal125.get_flight_info())
pal125.land()
print()

aa191 = Flight("AA191", ohare, lax, "2024-06-15 10:00", "2024-06-15 12:00", "American Airlines")
aa191.take_off()
print(aa191.get_flight_info())
aa191.crash()
print()

