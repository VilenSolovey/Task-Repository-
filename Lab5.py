from enum import Enum
from datetime import datetime


class CarBrand(Enum):
    TOYOTA = 1
    FORD = 2
    HONDA = 3
    BMW = 4
    MERCEDES = 5
    AUDI = 6


class Car:
    def __init__(self, brand, age, maxSpeed, horsePower):
        self.brand = brand
        self.age = age
        self.maxSpeed = maxSpeed
        self.horsePower = horsePower
        self.parked_time = None

    def __str__(self):
        return f"Brand: {self.brand}, Age: {self.age} years, Max Speed: {self.maxSpeed} km/h, Horsepower: {self.horsePower}"


class Parking:
    def __init__(self, max_capacity, hourly_rate):
        self.max_capacity = max_capacity
        self.hourly_rate = hourly_rate
        self.cars = []

    def parkCar(self, car):
        if len(self.cars) < self.max_capacity:
            car.parked_time = datetime.now()
            self.cars.append(car)
            print(f"{car.brand} is parked.")
        else:
            print("Parking is full. Cannot park the car.")

    def leaveParking(self, car):
        if car in self.cars:
            parked_time = car.parked_time
            parked_duration = (datetime.now() - parked_time).total_seconds() / 3600  # hours
            parking_cost = parked_duration * self.hourly_rate
            self.cars.remove(car)
            car.parked_time = None
            print(f"{car.brand} has left the parking. Parking cost: ${parking_cost:.2f}")
        else:
            print(f"{car.brand} is not in the parking.")

    def calculateParkingCost(self):
        for car in self.cars:
            parked_time = car.parked_time
            if parked_time:
                parked_duration = (datetime.now() - parked_time).total_seconds() / 3600  # hours
                parking_cost = parked_duration * self.hourly_rate
                print(f"{car.brand} has parked for {parked_duration:.2f} hours. Parking cost: ${parking_cost:.2f}")


def main():
    parking = Parking(max_capacity=5, hourly_rate=5.0)

    car1 = Car(CarBrand.TOYOTA, 3, 180, 150)
    car2 = Car(CarBrand.BMW, 2, 220, 300)
    car3 = Car(CarBrand.HONDA, 5, 160, 120)

    parking.parkCar(car1)
    parking.parkCar(car2)
    parking.parkCar(car3)

    parking.calculateParkingCost()

    parking.leaveParking(car1)


if __name__ == "__main__":
    main()
