import sys

def main():
    count = int(sys.argv[1]) + 1

    for i in range(1, count):
        if i%3 == 0:
            print("Fizz", end="")
        if i%5 == 0:
            print("Buzz", end="")
        if i%3 != 0 and i%5 != 0:
            print(str(i), end="")
        print()
    

main()
