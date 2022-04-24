import unittest
import fizz

class TestChrisdFizzBuzz(unittest.TestCase):
    def test_fizz(self):
        print("Testing Fizz not on 2")
        self.assertNotEqual("fizz", fizz.fizz(2).split()[-1].lower())
    def test_buzz(self):
        print("Testing buzz not on 4")
        self.assertNotEqual("buzz", fizz.fizz(4).split()[-1].lower())
    def test_ping(self):
        print("Testing ping ")
        self.assertEqual("ping", fizz.fizz(7).split()[-1].lower())
    def test_pong(self):
        print("Testing pong ")
        self.assertEqual("pong", fizz.fizz(11).split()[-1].lower())



