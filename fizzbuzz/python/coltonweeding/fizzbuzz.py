import sys

class FizzBuzz:

    def LoopFizzBuzz(self, number):
        for i in range(1, number + 1):
            print(self.FizzBuzz(i))

    def FizzBuzz(self, i):
        line = ""
        if (i % 3 == 0):
            line += "Fizz"
        if (i % 5 == 0):
            line += "Buzz"
        if (i % 7 == 0):
            line += "Ping"
        if (i % 11 == 0):
            line += "Pong"
        if not line:
            return i
        else:
            return line


if __name__ == "__main__":
    fizzbuzz = FizzBuzz()
    fizzbuzz.LoopFizzBuzz(int(sys.argv[1]))
