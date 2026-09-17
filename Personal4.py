class Airport:
    def __init__(self, name, code, city):
        self.name = name
        self.code = code
        self.city = city

    def get_info(self):
        return f"{self.name} ({self.code}) - {self.city}"