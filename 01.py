from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, make, model):
        self.make = make
        self.model = model

    @abstractmethod
    def start_engine(self):
        pass


class Car(Vehicle):
    def start_engine(self):
        print(f"{self.make} {self.model}: Двигун запущено")


class Motorcycle(Vehicle):
    def start_engine(self):
        print(f"{self.make} {self.model}: Мотор заведено")


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make, model):
        pass

    @abstractmethod
    def create_motorcycle(self, make, model):
        pass


class USVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(make, model)

    def create_motorcycle(self, make, model):
        return Motorcycle(make, model)


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(make, model)

    def create_motorcycle(self, make, model):
        return Motorcycle(make, model)


# Використання
us_factory = USVehicleFactory()
eu_factory = EUVehicleFactory()
us_factory.create_car("Us Spec", "Ford Focus").start_engine()
eu_factory.create_car("Eu Spec", "Audi A4").start_engine()
us_factory.create_motorcycle("Us Spec   ", "Harley Davidson").start_engine()
eu_factory.create_motorcycle("Eu Spec", "Ducati").start_engine()
