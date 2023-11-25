from enum import Enum
class Automobile:
    class Brand(Enum):
        BMW = 1
        Mercedes = 2
        Audi = 3
        Porsche = 4
        Tesla = 5

    def __init__(self, brand, age, max_speed, horse_power, parked_time):
        self.__brand = brand
        self.__age = age
        self.__max_speed = max_speed
        self.__horse_power = horse_power
        self.__parked_time = parked_time

    def get_brand(self):
        return self.__brand

    def get_age(self):
        return self.__age

    def get_max_speed(self):
        return self.__max_speed

    def get_horse_power(self):
        return self.__horse_power

    def get_parked_time(self):
        return self.__parked_time

    def calculate_parking_price(self, hourly_rate):
        return self.get_parked_time() * hourly_rate

    def __str__(self):
        return f"{self.__brand} (Age: {self.__age}, Max Speed: {self.__max_speed} km/h, Horse Power: {self.__horse_power} HP)"

class Parking:
    def __init__(self, max_capacity, hourly_rate):
        self.__max_capacity = max_capacity
        self.__hourly_rate = hourly_rate
        self.__cars = []

    def park_car(self, car):
        if len(self.__cars) < self.__max_capacity:
            self.__cars.append(car)
            print(
                f"{car} already parked for {car.get_parked_time()} hours. Current price is ${car.calculate_parking_price(self.__hourly_rate)}")
            self.display_overflow_status()

    def leave_parking(self, car):
        if car in self.__cars:
            hours_parked = car.get_parked_time()
            price = car.calculate_parking_price(self.__hourly_rate)
            print(f"{car} left the parking. Parking duration: {hours_parked} hours. Final price: ${price}")
            self.__cars.remove(car)

    def display_overflow_status(self):
        if len(self.__cars) == self.__max_capacity:
            print("Parking is full. No more spaces available.")

    def display_parking_status(self):
        print(f"Parking status: {len(self.__cars)} out of {self.__max_capacity} cars parked.")

    def parked_time_top(self):
        cars_sorted_by_parked_time = sorted(self.__cars, key=lambda car: car.get_parked_time(), reverse=True)
        return cars_sorted_by_parked_time

def main():
    parking_lot = Parking(max_capacity=5, hourly_rate=10)

    car1 = Automobile(Automobile.Brand.BMW, 3, 250, 300,1)
    car2 = Automobile(Automobile.Brand.Mercedes, 2, 220, 250,5)
    car3 = Automobile(Automobile.Brand.Audi, 4, 280, 350,16)
    car4 = Automobile(Automobile.Brand.Tesla, 1, 200, 400,12)
    car5 = Automobile(Automobile.Brand.Porsche, 2, 300, 450,15)

    parking_lot.park_car(car1)
    parking_lot.park_car(car2)
    parking_lot.park_car(car3)
    parking_lot.park_car(car4)
    parking_lot.park_car(car5)

    parking_lot.display_parking_status()
    parked_time_sorted_cars = parking_lot.parked_time_top()
    print("-----------------")
    print("Cars sorted by parked time:")
    for car in parked_time_sorted_cars:
        print(f"{car} - Parked time: {car.get_parked_time()} hours")
    print("-----------------")
    parking_lot.leave_parking(car2)
    parking_lot.display_parking_status()


    print("-----------")
if name == "__main__"
