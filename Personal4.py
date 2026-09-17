import datetime
class Airport:
    def __init__(self, name, code, city):
        self.name = name
        self.code = code
        self.city = city
        self.max_plane_capacity = 100
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
        print(f"{self.airline} Flight {self.flight_number} has taken off from {self.origin.get_info()}.")

    def land(self):
        if self.destination.current_plane_count < self.destination.max_plane_capacity:
            self.destination.current_plane_count += 1
            print(f"{self.airline} Flight {self.flight_number} has landed at {self.destination.get_info()}.")
        else:
            print(f"{self.airline} Flight {self.flight_number} cannot land. {self.destination.get_info()} has reached its maximum plane capacity.")





