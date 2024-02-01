from abc import ABC
from serviceable import Serviceable
from car_factrory import CarFactory
class Car(Serviceable,CarFactory, ABC):
    def __init__(self, engine ,battery):
        self.engine = engine
        self.battery = battery

   
