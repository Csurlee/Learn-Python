print("Let's play a simple math game")
print("Choose a number from 1 to 5.")

number = input("> ")

if number == "1":
	print("You loose! Bye!")
elif number == "2":
	print("You are in the right place")
	n2 = input("2+2? -> ")

	if n2 == "4":
		print("You are right!")
	else:
		print("You are wrong! Try harder!")
			return False


elif number == "3":
	print("You loose! Bye!")

elif number == "4":
	print("You loose! Bye!")

elif number == "5":
	print("You loose! Bye!")

else:
	print("Please choose a number from 1 to 5.")