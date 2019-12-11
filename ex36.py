from sys import exit


def start():
	print("You are at front of a door.")
	print("Go inside typing 'start'")
	print("For help and commands please type 'help'")

	choise = input("> ")

	if choise == "start":
		middle_room()
	else:
		help()




def middle_room():
	print("You have entered in the middle of the game.")
	print("This room is empty. There is  a door in your right, left, front, and back.")
	print("Which one do you take?")

	choise = input("> ")

	if choise == "left":
		left_room()
	elif choise == "right":
		right_room()
	elif choise == "front":
		front_room()
	elif choise == "back":
		back_room()
	else:
		help()




def left_room():
	print("You go left")
	print("Now open the door")

	choise = input("> ")

	if choise == "open":
		print("You are now in the left room.")
		print("In front of you is a BLACK MONSTER. what do you do?")
		bmonster_moved = False

		while True:
			choise = input("> ")

			if choise == "going home":
				dead("The monster looks at you and slaps your face off.")
			elif choise == "taunt monster" and not bmonster_moved:
				print("The monster has moved from the door.")
				print("You can go through now.")
				bmonster_moved = True
			elif choise == "taunt monster" and bmonster_moved:
				dead("The monster get pissed off and slaps you in the face.")
			elif choise == "go" and bmonster_moved:
				reward_room()
			else:
				print("I got no idea what that means.")
				help()



def right_room():
	print("right")


def front_room():
	print("front")


def back_room():
	print("back")


def dead(why):
	print(why, "You're dead!")
	exit(0)


def reward_room():
	print("You have reached the last room where you can choose how many gold do you want to get")
	print("Choose your number carefully if you take more that you can carry you can not go outside the door.")

	try:
		how_much = int(input("> "))
	except:
		dead("Man, learn to type a number")

	if how_much < 100:
		print("Nice, you're not greedy, you win! Now open the door and leave.")

		choise = input("> ")

		if choise == "open":
			print("Bye bye, see you soon")
			exit(0)
		else:
			print("You are penalized for wrong answer. You start from the beginning.")
			start()
	else:
		print("====================================================================")
		print("| You are greedy, you can not open the door. You're hands are full.|")
		print("| You start from the beginning.                                    |")
		print("====================================================================")
		start()		




def help():
	print("""Please use this commands:
		- Open a door: open
		- To go left: left
		- To go right: right
		- To go front: front
		- To go back: back
		- Go through the room now: go
		MONSTER:
		- taunt monster
		- going home
		""")
	




start()