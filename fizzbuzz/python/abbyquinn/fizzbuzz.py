# fizz buzz
# will take imputted number(n) form command line
# will print numbers 1 to n 
# all multiples of three will print fizz
# all multiples of five will print buzz

import sys

def fizzBuzz(val):
    val = int(val)
    for i in range(1,val+1):
        if i%3 == 0 and i%5 != 0:
            print("Fizz")
        if i%5 == 0 and i%3 != 0:
            print("Buzz")
        if i%5 == 0 and i%3 == 0:
            print("FizzBuzz")
        if i%3 != 0 and i%5 != 0:
            print(i)
              


def main(val):
    fizzBuzz(val)

main(int(sys.argv[1]))

