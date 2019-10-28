from sys import argv

script, filename = argv
y = 'y'


print(f"We are going to erase {filename}.")
print("If you don't want that, hit CTRL+C (^C).")
print("If you do want that, hit RETURN (ENTER).")

input("?")

print("Opening the file...")
target = open(filename, 'w') # Open the file

print("Truncating the file. Goodbey!")
target.truncate()

print("Now I'm going to ask you for three lines")
line1 = input("line 1:")
line2 = input("line 2:")
line3 = input("line 3:")
newline = "\n"

print("I'm going to write these lines to the file.")

##
# Writing lines in 1 line of code
##
target.writelines([line1, newline, line2, newline, line3, newline])


##
# Writing line per line
##
#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

print("do you want to list it?")
print("And finally we close it.")
target.close()