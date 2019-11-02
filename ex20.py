from sys import argv

script, input_file = argv

def print_all(f):   # printing the whole file finction
    print(f.read())
    print(f.tell())

def rewind(f):  # Seek file
    f.seek(0)

def print_a_line(line_count, f):    # Print a line from the file
    print(line_count, f.readline())

current_file = open(input_file)     # converting the input_file

print("first let's print The whole file: \n")

print_all(current_file)     # Calling the print_all function

print("now let's rewind kinde of like a tape")

rewind(current_file)    # Calling  the SEEK Function

print("let's print three lines")

current_line = 1 
print_a_line(current_line, current_file)        # Calling the print a line function

current_line += 1 # printing the 2nd line of the file line 1 from current_line + 1
print_a_line(current_line, current_file)

current_line += 1  # printing the 3th line of the file line 1 from current_line + 1 + 1
print_a_line(current_line, current_file)
# and so on..
