class Lab():
    def __init__(self, room_number):
        self.room_number = room_number

class Technician:
    def __init__(self, name, assigned_lab):
        self.assigned_lab = None
        self.name = name

    def assign_lab(self, lab_obj):
        self.assigned_lab = lab_obj

chem_lab = Lab("302")
mr_cruz = Technician("Mr.Cruz", chem_lab)
mr_cruz.assign_lab(chem_lab)
print(mr_cruz.assigned_lab.room_number)
