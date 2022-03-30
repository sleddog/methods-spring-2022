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

class TestFizzBuzz(unittest.TestCase):
    def testFizz(self):
        print("Testing Fizz ...")
        if (self.assertEqual("Fizz", fizzbuzz(3)) == None):
            print("Test Passed")
        else:
            print("Test Failed")

    def testBuzz(self):
        print("Testing Buzz ...")
        if (self.assertEqual("Buzz", fizzbuzz(5)) == None):
            print("Test Passed")
        else:
            print("Test Failed")

    def testFizzBuzz(self):
        print("Testing FizzBuzz ...")
        if (self.assertEqual("FizzBuzz", fizzbuzz(15)) == None):
            print("Test Passed")
        else:
            print("Test Failed")

    def test2(self):
        print("Testing 2 ...")
        if (self.assertEqual("2", fizzbuzz(2)) == None):
            print("Test Passed")
        else:
            print("Test Failed")

    def testPing(self):
        print("Testing Ping ...")
        if (self.assertEqual("Ping", fizzbuzz(7)) == None):
            print("Test Passed")
        else:
            print("Test Failed")

    def testPong(self):
        print("Testing Pong ...")
        if (self.assertEqual("Pong", fizzbuzz(11)) == None):
            print("Test Passed")
        else:
            print("Test Failed")

    def testFizzBuzzPingPong(self):
        print("Testing FizzBuzzPingPong ...")
        if (self.assertEqual("FizzBuzzPingPong", fizzbuzz(1155)) == None):
            print("Test Passed")
        else:
            print("Test Failed")