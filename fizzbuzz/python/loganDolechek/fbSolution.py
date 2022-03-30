#Fizz Buzz Solution
#Logan Dolechek
import unittest

def fizzbuzz(n):
   fizz = ""
   if n % 3 == 0:
      fizz += "Fizz"
   if n % 5 == 0:
      fizz += "Buzz"
   if n % 7 == 0:
      fizz += "Ping"
   if n % 11 == 0:
      fizz += "Pong"
   if (fizz == ""):
      fizz = string(n)
   return fizz



class TestFizzBuzz(unittest.TestCase):
   def testFizz(self):
      print("Testing Fizz")
      if (self.assertEqual("Fizz", fizzbuzz(3)) == None):
         print("Test Passed")
      else:
         print("Test Failed")

   def testBuzz(self):
      print("Testing Buzz")
      if (self.assertEqual("Buzz", fizzbuzz(5)) == None):
         print("Test Passed")
      else:
         print("Test Failed")

   def testFizzBuzz(self):
      print("Testing FizzBuzz")
      if (self.assertEqual("FizzBuzz", fizzbuzz(30)) == None):
         print("Test Passed")
      else:
         print("Test Failed")

   def testPing(self):
      print("Testing Ping")
      if (self.assertEqual("Ping", fizzbuzz(7)) == None):
         print("Test Passed")
      else:
         print("Test Failed")

   def testPong(self):
      print("Testing Pong")
      if (self.assertEqual("Pong", fizzbuzz(11)) == None):
         print("Test Passed")
      else:
         print("Test Failed")

   def testFizzBuzzPingPong(self):
      print("Testing FizzBuzzPingPong")
      if (self.assertEqual("FizzBuzzPingPong", fizzbuzz(1155)) == None):
         print("Test Passed")
      else:
         print("Test Failed")

