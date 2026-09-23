class Glassware:
    def __init__(self, name):
        self.name = name

    def dislay_info(self):
        return f"Glassware: {self.name}"

class Beaker(Glassware):
    def __init__(self, capacity):
        self.capacity = capacity

    super().__init__("Beaker")

class Tray:
    def __init__(self):
        self.beakers = Beaker(250) for _ in range(5)

    def print_contents(self):

        for i, beaker in enumerate(self.beakers):
            print(f"Beaker {i}", end="")

    

    