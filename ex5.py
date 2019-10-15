my_name = 'Laszlo J. Dembrovszky'
my_age = 35
my_height = round(74 / 39.3701) # inches to meter
my_weight = 180 / round(2.2) # lbs to kg
my_eyes = 'Braun'
my_theeth = 'White'
my_hair = 'Blond'

print(f"Let's talk about my {my_name}.")
print(f"He's {my_height} meter tall.")
print(f"He's {my_weight} KG heavy")
print("Actualy that's not so heavy")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_theeth} depending on the coffee.")

# this line in tricky

total = my_age + my_height + my_weight
print(f"if i add {my_age}, {my_height}, and {my_weight} I get {total}.")
