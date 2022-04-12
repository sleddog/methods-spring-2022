import unittest

def fizzbuzz(n):
    stringOut = ""
    if n%3 == 0:
        stringOut += "Fizz"
    if n%5 == 0: 
        stringOut += "Buzz"
    if n%7 == 0:
        stringOut += "Ping"
    if n%11 == 0:
        stringOut += "Pong"
    if (n%3 != 0 and n%5 != 0 and n%7 != 0 and n%11 != 0): 
        stringOut += str(n)
    return stringOut
