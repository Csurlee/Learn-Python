types_of_people = 10
x = f"There are {types_of_people} types of people"

binary = "binary"
do_not = "don't"
y = f"those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"i said: {x}")
print(f"i also said: '{y}'")

hilarios = False
joke_evaluation = "Isn't that joke so funny?! {}"
print(joke_evaluation.format(hilarios))

w = "This is the left side of ..."
e = "a string with a roght side"

print(w + e)