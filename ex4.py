cars = 100
space_in_a_car = 4.0
drivers = 30
passangers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
avarage_passengers_per_car = passangers / cars_driven

print("there are", cars, "cars available.")
print("there are only", drivers, "drivers available.")
print("there will be", cars_not_driven, "empty cars today.")
print("we can transport", carpool_capacity, "people today.")
print("we have", passangers, "to carpoll today.")
print("we need to put about", avarage_passengers_per_car, "in each car")
