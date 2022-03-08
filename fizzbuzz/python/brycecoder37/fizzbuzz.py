# ------------------------------------------
# This is a Python program to solve FizzBuzz
# ------------------------------------------

import sys

# -------------------------------------------------------
# fizzBuzz takes in an integer x and then tests, for all
# integers 1 through x, whether that number is divisible 
# by 3 and 5. It will print certain messages depending on
# whether it is divisible by 3, 5, both, or neither.
# -------------------------------------------------------

def fizzBuzz(num):
    for i in range(1, num+1):
        line_to_print = ""
        if (i % 3 == 0):
            line_to_print += "Fizz"
        if (i % 5 == 0):
            line_to_print += "Buzz"
        
        if (line_to_print == ""):
            print(i)
        else:
            print(line_to_print)

# -------------------------------------------

def main(number):
    fizzBuzz(number)

# Run main using the command line argument

main(int(sys.argv[1]))

