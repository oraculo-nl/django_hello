class Motor:
    def __init__(self, brandstof, vermogen):
        self.vermogen = vermogen
        self.brandstof = brandstof

class Benzinemotor(Motor):
    def __init__(self):
        super().__init__("benzine", 150)

class Dieselmotor(Motor):
    def __init__(self):
        super().__init__("diesel", 200)

class Auto:
    def __init__(self, motor, merk):
        self.motor = motor
        self.merk = merk


auto = None

print(auto.motor.vermogen)

# auto = Auto(Benzinemotor(), "BMW")
#
# print(auto.motor.brandstof)
#
# auto2  = Auto(Dieselmotor(), "Mercedes")