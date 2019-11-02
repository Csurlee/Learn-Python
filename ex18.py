# this is like argv

def print_two(*args):
    arg1, arg2 =args
    print(f"arg1: {arg1}, arg2: {arg2}")

# 2nd metod

def print_two_again(arg1, arg2):
    print(f"1 {arg1}, 2 {arg2}")

def print_one(arg1):
    print(f"1.  {arg1}")

def print_none():
    print("i got nothing")

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("Zed")
print_none()