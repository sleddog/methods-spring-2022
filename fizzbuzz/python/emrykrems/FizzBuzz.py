import sys

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

FizzBuzz(int(sys.argv[1]))
