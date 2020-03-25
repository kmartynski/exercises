
class IllegalCarError(Exception):
    def __init__(self, message, errors):
        super().__init__(message)
        self.errors = errors
        print('Printing Errors:')
        print(errors)


class Car:
    def __init__(self, pax_count, car_mass, gear_count):
        self.set_pax(pax_count)
        self.set_mass(car_mass)
        self.set_gear(gear_count)

    def get_pax(self):
        return self.__pax_count

    def get_mass(self):
        return self.__car_mass

    def get_gear(self):
        return self.__gear_count

    def set_pax(self, pax_count):
        if pax_count < 1 or pax_count > 5:
            raise IllegalCarError("Raised when the car is illegal", "Too many passengers!")
        else:
            self.__pax_count = pax_count

    def set_mass(self, car_mass):
        if car_mass > 2000:
            raise IllegalCarError("Raised when the car is illegal", "The mass is too high!")
        else:
            self.__car_mass = car_mass

    def set_gear(self, gear_count):
        self.__gear_count = gear_count

    @property
    def total_mass(self):
        return (self.__pax_count * 70) + self.__car_mass

    def __str__(self):
        return f"The car has {self.__pax_count} passangers (incl. one driver of course).\n" \
               f"It's total mass is equal to {self.total_mass} kg and has {self.__gear_count} gears."

c = Car(3, 1500, 5)
print(c)
print(c.total_mass)
print(c.get_mass())
print(c.get_gear())
print(c.get_pax())

class Vehicle:
    def __init__(self, name):
        self.name = name

    def repair(self):
        print(f"The {self.name} is being repaired!")

class Workshop:

    def accept(self, vehicle):
        vehicle.repair()

b = Vehicle("Bicycle")
t = Vehicle("Truck")
m = Vehicle("Car")
w = Workshop()

w.accept(b)
w.accept(t)
w.accept(m)



