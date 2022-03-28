import sys
class FizzBuzz:

    def __init__(self, number):
        self.number = number
        self.line = ""

    def FizzBuzz(self):
        line = ""

        for i in range(1, self.number + 1):
            if (i % 3 == 0):
                line += "Fizz"
            if (i % 5 == 0):
                line += "Buzz"
            if not line:
                print(i)
            else:
                print(line)
            line = ""

def main():
    fizzbuzz = FizzBuzz(int(sys.argv[1]))
    fizzbuzz.FizzBuzz()

main()
