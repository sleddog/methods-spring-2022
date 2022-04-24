import unittest
import sys


def fizz(num):
    for i in range(num+1):
        if (i % 3 == 0):
            print("fizz", end = "")
        if (i % 5 == 0):
            print("buzz", end = "")
        if(i % 3 > 0 and i % 5 > 0 and i % 7 > 0 and i % 11 > 0):
            print(i, end = "")
        if (i % 7 == 0):
            print("ping", end = "")
        if (i % 11 == 0):
            print("pong", end = "")
        print()

fizz(int(sys.argv[1]))