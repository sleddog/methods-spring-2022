import sys

def fizzbuzz(count):
    stringOut = ""

    for i in range(1, count):
        if i%3 == 0: stringOut += "Fizz"
        if i%5 == 0: stringOut += "Buzz"
        if (i%3 != 0 and i%5 != 0): stringOut += str(i)
        stringOut += "\n"

    return stringOut
    
print(fizzbuzz(int(sys.argv[1]) + 1))
