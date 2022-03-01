import sys

def fizz(num):
    for i in range(num+1):
        if (i % 3 == 0):
            print("fizz ")
        if (i % 5 == 0):
            print("buzz")
        if(i % 3 > 0 and i % 5 > 0):
            print(i)

fizz(int(sys.argv[1]))