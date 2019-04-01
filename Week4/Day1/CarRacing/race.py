import json


def read_json_cars_data():
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


def get_drviers_stats(cars_data):
    people = cars_data["people"]
    return [(person["name"], person["car"],
             person["model"],person["max_speed"])
            for person in people]


def build_drivers_list(drivers_stats):
    drivers_list = []
    print(drivers_stats)
    for name, car, model, ms in drivers_stats:
        drivers_list.append(Driver(name, Car(car, model, ms)))
    return drivers_list


class Car:
    def __init__(self, car, model, max_speed):
        self.car = car
        self.model = model
        self._max_speed = max_speed

    def __str__(self):
        return f'{self.car}, {self.model}, {self._max_speed}'

    def get_max_speed(self):
        return self._max_speed


class Driver:
    def __init__(self, name, car):
        self.name = name
        self.car = car

    def __str__(self):
        return f'{self.name}'


class Race:
    def __init__(self, drivers, crash_chances):
        self.drivers = drivers
        self.crash_chances = crash_chances

    def __getitem__(self, item):
        return self.drivers[item]

    def result(self):pass


if __name__ == '__main__':
    json_data = read_json_cars_data()
    drivers_stats = get_drviers_stats(json_data)
    list_of_drivers = build_drivers_list(drivers_stats)
    for driver in list_of_drivers:
        print(driver)