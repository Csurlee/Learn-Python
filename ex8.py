# format() is to format the formatter
# The {} is where the format() will put the data in the ()


formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "blah blah blah",
    "lala lala lala",
    "bbb bbb bb b bbb",
    "rrr rrr rrr"
))
