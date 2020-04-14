import mystuff_ex40
mystuff_ex40.apple()
print(mystuff_ex40.tangerine)


#mystuff_ex40['apple'] # from dict
#mystuff_ex40.apple() # from the module
#mystuff_ex40.tangerine() # module with variable
print("----")

class Mystuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I AM CLASSY APPLES!")
thing = Mystuff()
thing.apple()
print(thing.tangerine)
