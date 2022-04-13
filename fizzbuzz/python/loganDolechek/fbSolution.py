#Fizz Buzz Solution
#Logan Dolechek
import sys


def fizzbuzz(n):

    for fb in range(1,n+1):
        if fb % 1155 == 0:
          print("FizzBuzzPingPong")
          continue
        if fb % 15 == 0:
          print("FizzBuzz")
          continue
        elif fb % 3 == 0:
           print("Fizz")
           continue
        elif fb % 5 == 0:
           print("Buzz")
           continue
        elif fb % 7 == 0:
           print("Ping")
           continue
        elif fb % 11 == 0:
           print("Pong")
           continue
        print(fb)

fizzbuzz(int(sys.argv[1]))
