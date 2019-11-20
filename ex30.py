people = 10
cars = 40
trucks = 15

if cars > people:
	print("We should take the cars")

elif cars < people:
	print("We should npt take the cars")

else:
	print("we can't decide")

if trucks > cars:
	print("Thats's too many trucks")

elif trucks < cars:
	print("Maybe we can take the trucks")

else:
	prin("We still can't decide")

if people > trucks:
	print("Alright, let's just take the trucks")

else:
	print("Fine, let's stay home")

if cars > people or trucks < cars:
	print("This is True")

else:
	print("This is not True")