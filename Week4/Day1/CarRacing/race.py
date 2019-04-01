import json
import random

class CrashChangeGenerator:
    def __init__(self, a=0, b=1):
        self.a = a
        self.b = b
    
    def generate_crash_chance(self):
        chance = f'{random.uniform(self.a, self.b):.2f}'
        return float(chance)

    def generate_chance_for_drivers(self, drivers):
        return [self.generate_crash_chance() 
                for _ in range(len(drivers))]


class JsonParser:
    def __init__(self, json_file):
        self.parsed_data = JsonParser.read_json_cars_data(json_file)

    def get_drviers_stats(self):
        people = self.parsed_data["people"]
        return [(person["name"], person["car"],
                 person["model"],person["max_speed"])
                for person in people]
    

    @staticmethod
    def read_json_cars_data(json_file):
        try:
            with open('cars.json') as jf:
                try:
                    cars_data = json.load(jf)
                    return cars_data
                except ValueError:
                    print('Error, file specified not in json format!')
                    exit(-1)
        except FileNotFoundError:
            print('Error, file specified not found!')
            exit(-1)


class Car:
    def __init__(self, car, model, max_speed):
        self.car = car
        self.model = model
        self.max_speed = max_speed

    def __str__(self):
        return f'{self.car}, {self.model}, {self.max_speed}'

    def __repr__(self):
        return str(self)


class Driver:
    def __init__(self, name, car):
        self.name = name
        self.car = car

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return str(self)

    def get_speed(self):
        return self.car.max_speed

    @classmethod
    def build_drivers_list(cls, drivers_data):
        drivers_list = []
        for name, car, model, ms in drivers_data:
            drivers_list.append(cls(name, Car(car, model, ms)))
        return drivers_list


class Race:
    def __init__(self, drivers, crash_chances):
        self.drivers = drivers
        self.crash_chances = crash_chances

    def __getitem__(self, item):
        return self.drivers[item]

    def result(self):
        drivers_with_chances = list(zip(self.drivers, self.crash_chances))
        avg = sum(self.crash_chances)/len(self.crash_chances)
        filtered_drivers = Race._filter_drivers(avg, drivers_with_chances)
        filtered_drivers.sort(key=lambda driver: driver[0].get_speed(), reverse=True)
        return filtered_drivers
        
    @staticmethod
    def _filter_drivers(avg, drivers_with_chances):
        return [driver for driver in drivers_with_chances
                if driver[1] > avg]


if __name__ == '__main__':
    gcc = CrashChangeGenerator()
    drivers_stats = JsonParser('cars.json').get_drviers_stats()
    drivers_list = Driver.build_drivers_list(drivers_stats)
    crash_chance = gcc.generate_chance_for_drivers(drivers_list)
    race = Race(drivers_list, crash_chance)
    print(race.result())