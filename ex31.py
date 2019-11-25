print(""" You enter ins a dark room with two doors.
Do you go through door #1 or door #2? """)

door = input("> ")

if door == "1":
	print("(1.)There's  a giant bear here eating a cheese cake.")
	print("(1.)What do you do?")
	print("(1.)1. Take the cake.")
	print("(1.)2. Scream at the bear.")

	bear = input("> ")

	if bear == "1":
		print("(1.1) The bear eats your face off. Good job!")
	elif bear == "2":
		print("(1.2) The bear eats your legs off. Good job! ")
	else:
		print(f"(1.3) Well, doing {bear} is probably better.")
		print("(1.4) Bear runs away")

elif door == "2":
	print("(2.) You stare into the endless abyss at Cthulhu's retina.")
	print("(2.) 1. Blueberries.")
	print("(2.) 2. Yellow jacket clothespins.")
	print("(2.) 3. Understanding revolvers yelling melodies.")

	insanity = input("> ")

	if insanity == "1" or insanity == "2":
		print("(2.1) Your body survives powered by a mind of jello.")
		print("(2.2) Good job!")
	else:
		print("(2.3) The insanity rots your eyes into a pool of muck.")
		print("(2.4) Good job!")

else:
	print("You stumble around and fall on a knife and die. Good job!")	