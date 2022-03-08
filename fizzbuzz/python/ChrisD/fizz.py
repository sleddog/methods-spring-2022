import sys

def fizz(num):
    for i in range(num+1):
        if (i % 3 == 0):
            print("fizz", end = "")
        if (i % 5 == 0):
            print("buzz", end = "")
        if(i % 3 > 0 and i % 5 > 0):
            print(i, end = "")
        print()

fizz(int(sys.argv[1]))