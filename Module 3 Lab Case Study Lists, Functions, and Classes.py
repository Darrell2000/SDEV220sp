"""Darrell Davis
   04/02/2025
   Module 3 Lab - Case Study: Lists, Functions, and Classes"""

# Writing a code that will define a super class car. It will ask user for specific information it will ask 
# for vehicle type, year, make, model, doors, roof and output the information given.

# Define the superclass Vehicle
class Vehicle:
    def __init__(self, vehicle_type):

        # Store the type of vehicle (e.g., car, truck, boat, etc.)

        self.vehicle_type = vehicle_type

# Define the subclass Automobile that inherits from Vehicle

class Automobile(Vehicle):

    def __init__(self, vehicle_type, year, make, model, doors, roof):

        # Initialize the vehicle_type using the parent class

        super().__init__(vehicle_type)

        # Set additional attributes specific to automobiles
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

# Store a default vehicle type as "car"
vehicle_type = "car"

# Get user input for automobile attributes
year = input("Enter the year: ")
make = input("Enter the make: ")
model = input("Enter the model: ")
doors = input("Enter the number of doors (2 or 4): ")
roof = input("Enter the type of roof (solid or sun roof): ")

# Create an instance of the Automobile class using the input values
car = Automobile(vehicle_type, year, make, model, doors, roof)

# Display the car's information in a readable format
print("\nVehicle type:", car.vehicle_type)
print("Year:", car.year)
print("Make:", car.make)
print("Model:", car.model)
print("Number of doors:", car.doors)
print("Type of roof:", car.roof)