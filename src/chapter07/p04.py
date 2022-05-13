"""
**Parking Lot**:

 Design a parking lot using object-oriented principle
"""

# Objects
# * Car
# * Spots
# * Payment

# Actions
# * park
# * enter
# * exit

# Questions:
# * Do we care about the vehicule type? (Car, Bus, Mo
# * Should we model types of car spots? (Disabled/Standard)
# * Is it a paying parking lot? Should we model for extensibility (Free/Paying)?

# Story:
# A vehicule wants to park in a parking lot. The parking lot indicates to the driver how many parking spots are still available.
# The parking lot has multiple stories, each with a certain number of available parking spots. Each parking spot is adapted for a certain size of vehicule.
# The parking lot supports buses, bikes, motorbikes, and cars. In addition the parking lot has priority spots for disabled passengers.
# Each spot supports a space for a smaller vehicule, except for bikes which are limited to be stored in a ike rake.


from dataclasses import dataclass, field
from typing import List, Dict, Type
from collections import ChainMap


@dataclass
class ParkingSpot:
    size: int
    number: int


@dataclass
class CarParkingSpot(ParkingSpot):
    size: int = 20


@dataclass
class BusParkingSpot(ParkingSpot):
    size: int = 40


@dataclass
class MotorCycleParkingSpot(ParkingSpot):
    size: int = 5


@dataclass
class Vehicle:
    size: int
    has_disabled_passenger: bool = False
    parking_spot: ParkingSpot = field(default=None)

    def park(self, parking_spot: ParkingSpot):
        if self.can_park(parking_spot):
            self.parking_spot = parking_spot

    def can_park(self, parking_spot: ParkingSpot):
        return parking_spot.size >= self.size

    @property
    def type(self):
        return type(self)


@dataclass
class Car(Vehicle):
    size: int = 20


@dataclass
class Bus(Vehicle):
    size: int = 40


@dataclass
class MotorCycle(Vehicle):
    size: int = 5


class Floor:
    spots: Dict[Type[Vehicle], List[ParkingSpot]]
    parked_vehicles: List[Vehicle]

    @property
    def total_space(self):
        return

    def has_available_space(self, vehicle: Vehicle):
        vehicle_type = type(vehicle)
        return bool(self.spots.get(vehicle_type))

    def park_vehicle(self, vehicle: Vehicle):
        if self.has_available_space(vehicle):
            self.parked_vehicles.append(vehicle)
            parking_spot = self.spots[vehicle.type].pop()
            vehicle.park(parking_spot)


class ParkingLot:
    floors: List[Floor]

    def has_available_space(self, vehicle: Vehicle):
        return bool(floor.has_available_space(vehicle) for floor in self.floors)

    def next_available_floor(self, vehicle: Vehicle):
        return next(
            floor for floor in self.floors if floor.has_available_space(vehicle)
        )

    @property
    def all_spots(self):
        spots = ChainMap(*(floor.spots for floor in self.floors))
        return spots

    def park_vehicle(self, vehicle: Vehicle):
        floor = self.next_available_floor(vehicle)
        floor.park_vehicle(vehicle)
