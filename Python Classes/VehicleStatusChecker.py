import random

class Vehcle:
    def __init__(self, vehicleName, vehicleColor, vehicleType, status):
        self.vehicleName = vehicleName
        self.vehicleColor = vehicleColor
        self.vehicleType = vehicleType
        self.status = status

    # vehicle info method
    def display_details(self):
        print("Vehicle Name : {}".format(self.vehicleName))
        print("Vehicle Color: {}".format(self.vehicleColor))
        print("Vehicle Type: {}".format(self.vehicleType))
        print("Vehicle Availability: {}".format("Available" if self.status else "Sold"))

    # vehicle availability update
    def update_status(self,new_status):
        self.status = new_status
        if new_status:
            print("{} is now available for sale".format(self.vehicleName))
        else:
            print("{} has been sold".format(self.vehicleName))

# Vehicles available for sale
car1 = Vehcle("Ford Mustang", "Black", "Gasoline", status=True)
car2= Vehcle("Toyota Prius","Red","Hybrid",status=True)
car3 = Vehcle("Honda Fit","Blue", "Hybrid",status=False)
car4 = Vehcle("Mazda Axela","Silver","Electric",status=True)

print("--- Autozone Vehicle Stocks ---")
print("\n")

car1.display_details()
print("\n")
car1.display_details()
print("\n")
car1.display_details()

print("\n")
print("\n")

# Update the vehilce is available
car3.update_status(True)
print("\n")
car1.update_status(False)
print("\n")

# displaying the updated veheicle
print("--- Vehicles updated ---")
car3.display_details()
print("\n")
car1.display_details()






