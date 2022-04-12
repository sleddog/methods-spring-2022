import sys


def fizzbuzz(n):
    for num in range(1, n + 1):
        if num % 15 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)


def main(number):
    fizzbuzz(number)


# Run main using the command line argument

main(int(sys.argv[1]))
