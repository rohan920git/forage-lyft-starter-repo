from abc import ABC, abstractmethod
from car_factrory import CarFactory
from car import Car
 

class Battery(Car,CarFactory,ABC):
    pass