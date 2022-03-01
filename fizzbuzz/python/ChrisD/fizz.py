import sys

def fizz(num):
    for i in num:
        if (num % 3 == 0):
            print("fizz ")
        if (num % 5 == 0):
            print("buzz")
        if(num % 3 > 0 and num % 5 > 0):
            print(num)

fizz(int(sys.argv[1]))