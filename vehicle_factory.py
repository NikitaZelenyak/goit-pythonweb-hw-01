from abc import ABC, abstractmethod
import logging

logging.basicConfig(
    format="%(asctime)s %(message)s",
    level=logging.DEBUG,
    handlers=[logging.FileHandler("vehicle_logging.log"), logging.StreamHandler()],
)


class Vehicle(ABC):
    def __init__(self, make: str, model: str) -> None:
        self.make = make
        self.model = model

    @abstractmethod
    def start_engine(self) -> None:
        pass


class Car(Vehicle):
    def start_engine(self) -> None:
        logging.info("%s %s: Двигун запущено", self.make, self.model)


class Motorcycle(Vehicle):
    def start_engine(self) -> None:
        logging.info("%s %s: Мотор заведено", self.make, self.model)


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> Car:
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        pass


class USVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model)

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, model)


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model)

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, model)


# Використання
us_factory = USVehicleFactory()
eu_factory = EUVehicleFactory()
us_factory.create_car("Us Spec", "Ford Focus").start_engine()
eu_factory.create_car("Eu Spec", "Audi A4").start_engine()
us_factory.create_motorcycle("Us Spec", "Harley Davidson").start_engine()
eu_factory.create_motorcycle("Eu Spec", "Ducati").start_engine()
