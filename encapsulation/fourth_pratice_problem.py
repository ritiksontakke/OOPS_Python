# ============================================================
# PILLAR: Encapsulation
# PROGRAM 4: Car Speed and Fuel
# ============================================================
#
# PROBLEM:
# Create a Car class that manages speed and fuel privately.
# - __speed starts at 0, max is 200 km/h
# - __fuel starts at given amount, max tank is 60 litres
# - accelerate(kmh): increases speed (uses 1 litre per 10 kmh increase)
#   - cannot accelerate if no fuel
#   - speed cannot exceed 200
# - brake(kmh): decreases speed (minimum 0)
# - refuel(litres): add fuel (cannot exceed 60 litres)
# - status(): print current speed and fuel
#
# EXAMPLE USAGE:
#   car = Car("Toyota", 20)
#   car.accelerate(50)
#   car.status()         # Speed: 50 km/h | Fuel: 15.0 L
#   car.brake(20)
#   car.status()         # Speed: 30 km/h | Fuel: 15.0 L
#   car.refuel(10)
#   car.status()         # Speed: 30 km/h | Fuel: 25.0 L
# ============================================================

class Car: 
    MAX_SPEED = 200
    MAX_FULE = 60

    def __init__(self, modul, fuel):
        self.modul = modul
        self.__speed = 0
        self.__fule = min(fuel, Car.MAX_FULE)

    def accelerate(self, kmh):
        if self.__fule < 0:
            print("fuel no enogh")
            return
        
        max_possible = self.__fule * 10
        actule_increase = min(kmh, max_possible)

        if self.__speed + actule_increase > Car.MAX_SPEED:
            actule_increase = Car.MAX_SPEED - self.__speed

        fuel_used = actule_increase / 10

        self.__speed += actule_increase
        self.__fule -= fuel_used

    def brake(self, kmh):
        self.__speed = max(0, self.__speed - kmh)
    def refule(self, liters):
        self.__fule = min(Car.MAX_FULE, self.__fule + liters)

    def status(self):
        print(f"Speed : {self.__speed} km/h | Fuel: {self.__fule:.1f} L")
    
car = Car("Toyota", 20)

car.accelerate(50)
car.status()    # Speed: 50 km/h | Fuel: 15.0 L

car.brake(20)
car.status()    # Speed: 30 km/h | Fuel: 15.0 L

car.refule(10)
car.status()    # Speed: 30 km/h | Fuel: 25.0 L