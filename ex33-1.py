
## Study Drills 


i = 0
numbers = []
v = i < 6


def my_list():
	global i, v
	while v:
		print(f"At the top i is {i}")
		numbers.append(i)

		i = i + 1
		print("Numbers now: ", numbers)
		print(f"At the bottom i is {i}")
		pass
my_list()
print("The numbers: ")

for num in numbers:
	print(num)