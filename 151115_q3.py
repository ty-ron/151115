# 151115_q3.py

# Import necessary libraries
import json

class Vehicle:
    def __init__(self, registration_number, make, model):
        self.registration_number = registration_number
        self.make = make
        self.model = model

class Car(Vehicle):
    def __init__(self, registration_number, make, model, number_of_seats):
        super().__init__(registration_number, make, model)
        self.number_of_seats = number_of_seats

class Truck(Vehicle):
    def __init__(self, registration_number, make, model, cargo_capacity):
        super().__init__(registration_number, make, model)
        self.cargo_capacity = cargo_capacity

class Motorcycle(Vehicle):
    def __init__(self, registration_number, make, model, engine_capacity):
        super().__init__(registration_number, make, model)
        self.engine_capacity = engine_capacity

class Fleet:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
        print("Vehicle added successfully!")

    def display_vehicles(self):
        if not self.vehicles:
            print("No vehicles found.")
        else:
            for vehicle in self.vehicles:
                print(f"Registration Number: {vehicle.registration_number}, Make: {vehicle.make}, Model: {vehicle.model}")

    def search_vehicle(self, registration_number):
        for vehicle in self.vehicles:
            if vehicle.registration_number.lower() == registration_number.lower():
                print(f"Found vehicle - Registration Number: {vehicle.registration_number}, Make: {vehicle.make}, Model: {vehicle.model}")
                return
        print("Vehicle not found.")

# Function to load vehicles from a JSON file
def load_vehicles(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            fleet = Fleet()
            for vehicle_data in data:
                if vehicle_data['type'] == 'car':
                    vehicle = Car(vehicle_data['registration_number'], vehicle_data['make'], vehicle_data['model'], vehicle_data['number_of_seats'])
                elif vehicle_data['type'] == 'truck':
                    vehicle = Truck(vehicle_data['registration_number'], vehicle_data['make'], vehicle_data['model'], vehicle_data['cargo_capacity'])
                elif vehicle_data['type'] == 'motorcycle':
                    vehicle = Motorcycle(vehicle_data['registration_number'], vehicle_data['make'], vehicle_data['model'], vehicle_data['engine_capacity'])
                fleet.add_vehicle(vehicle)
            return fleet
    except FileNotFoundError:
        return Fleet()

# Function to save vehicles to a JSON file
def save_vehicles(filename, fleet):
    with open(filename, 'w') as file:
        data = []
        for vehicle in fleet.vehicles:
            vehicle_data = {
                'registration_number': vehicle.registration_number,
                'make': vehicle.make,
                'model': vehicle.model
            }
            
