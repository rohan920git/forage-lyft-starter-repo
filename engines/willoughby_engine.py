from abc import ABC

from utils.engine import Engine


class WilloughbyEngine(Engine, ABC):
    def __init__(self ,last_service_mileage, current_mileage ):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def need_service(self):
        return self.current_mileage - self.last_service_mileage > 60000
