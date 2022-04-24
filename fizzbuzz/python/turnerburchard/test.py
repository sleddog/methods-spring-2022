import unittest
import fizzbuzz

class TestFizzBuzz(unittest.TestCase):
    def testFizz(self):
        print("Testing Fizz ...")
        if (self.assertEqual("Fizz", fizzbuzz.fizzbuzz(3)) == None):
            print("Test Passed")
        else:
            print("Test Failed")

    def testBuzz(self):
        print("Testing Buzz ...")
        if (self.assertEqual("Buzz", fizzbuzz.fizzbuzz(5)) == None):
            print("Test Passed")
        else:
            print("Test Failed")

    def testFizzBuzz(self):
        print("Testing FizzBuzz ...")
        if (self.assertEqual("FizzBuzz", fizzbuzz.fizzbuzz(15)) == None):
            print("Test Passed")
        else:
            print("Test Failed")

    def test2(self):
        print("Testing 2 ...")
        if (self.assertEqual("2", fizzbuzz.fizzbuzz(2)) == None):
            print("Test Passed")
        else:
            print("Test Failed")

    def testPing(self):
        print("Testing Ping ...")
        if (self.assertEqual("Ping", fizzbuzz.fizzbuzz(7)) == None):
            print("Test Passed")
        else:
            print("Test Failed")

    def testPong(self):
        print("Testing Pong ...")
        if (self.assertEqual("Pong", fizzbuzz.fizzbuzz(11)) == None):
            print("Test Passed")
        else:
            print("Test Failed")

    def testFizzBuzzPingPong(self):
        print("Testing FizzBuzzPingPong ...")
        if (self.assertEqual("FizzBuzzPingPong", fizzbuzz.fizzbuzz(1155)) == None):
            print("Test Passed")
        else:
            print("Test Failed")