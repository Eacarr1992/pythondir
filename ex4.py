#variable defined for cars. 100 is an integer
cars = 100
#variable defined for space_in_a_car. 4.0 is a float
space_in_a_car = 4.0
#variable defined for drivers. 30 is an integer
drivers = 30
#variable defined for passengers. 90 is an integer
passengers = 90
#variable defined for cars_not_driven. cars and drivers are integers and can be subtracted
cars_not_driven = cars - drivers
#variable cars_driven is defined as drivers. drivers is an integer
cars_driven = drivers
#variable defined for carpool_capacity. cars_driven is an integer and space_in_a_car is a float. not sure how these multiply properly
carpool_capacity = cars_driven * space_in_a_car
#variable defined for average_passengers_per_car. passengers and cars_driven are both integers and can be divided
average_passengers_per_car = passengers / cars_driven

#print strings with variables separated by commas.
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers avialable.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

#For error name car_pool_capacity not defined, the variable car_pool_capacity is not defined prior to being called. should be carpool_capacity
