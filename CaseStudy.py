class Vehicle:
    def __init__ (self, vehicle_type: str = None): 
        self.vehicle_type = vehicle_type


class Automobile(Vehicle):
    def __init__(self, vehicle_type:str, year, make, model, number_of_doors, type_of_roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.number_of_doors = number_of_doors
        self.type_of_roof = type_of_roof

    def printed_car(self):
        print(f"Vehicle Type: {self.vehicle_type}\n"
              f"Year: {self.year}\n"
              f"Make: {self.make}\n"
              f"Model: {self.model}\n"
              f"Number of Doors: {self.number_of_doors}\n"
              f"Type of Roof: {self.type_of_roof}\n")
 
get_vehicle_type = input("What type of vehicle do you drive?: ")
personal_vehicle = Vehicle(get_vehicle_type)
enter_year = input("What year is your vehicle?: ")
enter_make = input("What make is your vehicle?: ")
enter_model = input("What model is your vehicle?: ")
enter_doors = input("How many doors does your vehicle have?: ")
enter_roof = input("What kind of roof does your vehicle have?: ")
your_vehicle = Automobile(get_vehicle_type, enter_year, enter_make, enter_model, enter_doors, enter_roof)
your_vehicle.printed_car()