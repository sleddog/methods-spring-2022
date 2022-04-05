import sys

# FizzBuzz function receives an integer from command line input
# and tests from 1 to that integer if the number is divisible by
# 3 or 5. If divisible by 3, print "Fizz", if divisible by 5, print
# "Buzz", if divisible by 3 and 5, print "FizzBuzz".

def runFizzBuzz(number):
    for num in range(1,number+1):
        print(FizzBuzz(num))

def FizzBuzz(num):
    line_to_return = ""
    if (num % 3 == 0):
        line_to_return += "Fizz"
    if (num % 5 ==0):
        line_to_return += "Buzz"
    if (num % 7 == 0):
        line_to_return += "Ping"
    if (num % 11 == 0):
        line_to_return += "Pong"

    if not line_to_return:
        return (num)
    else:
        return (line_to_return)

# main funtion receives integer entered from command line
# and calls FizzBuzz() function with that integer as an argument

if __name__ == "__main__":
    input_number = int(sys.argv[1])
    runFizzBuzz(input_number)

