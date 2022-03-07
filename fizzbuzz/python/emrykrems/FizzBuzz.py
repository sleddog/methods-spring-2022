import sys

# FizzBuzz function receives an integer from command line input
# and tests from 1 to that integer if the number is divisible by
# 3 or 5. If divisible by 3, print "Fizz", if divisible by 5, print
# "Buzz", if divisible by 3 and 5, print "FizzBuzz".

def FizzBuzz(input_number):
    line_to_print = ""
    for num in range(1, input_number+1):
        if (num % 3 == 0):
            line_to_print += "Fizz"
        if (num % 5 ==0):
            line_to_print += "Buzz"
        if not line_to_print:
            print(num)
        else:
            print(line_to_print)
        line_to_print = ""

# main funtion receives integer entered from command line
# and calls FizzBuzz() function with that integer as an argument

def main(input_number):
    FizzBuzz(input_number)

main(int(sys.argv[1]))
