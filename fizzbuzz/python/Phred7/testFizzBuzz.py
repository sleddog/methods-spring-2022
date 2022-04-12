import unittest
import fizz_buzz

class TestFizzBuzz(unittest.TestCase):
    def test_fizz(self):
        print("Testing Fizz ...")
        self.assertEqual("fizz", fizz_buzz.fizz_buzz(3).split()[-1].lower())

    def test_buzz(self):
        print("Testing Buzz ...")
        self.assertEqual("buzz", fizz_buzz.fizz_buzz(5).split()[-1].lower())

    def test_ping(self):
        print("Testing Ping ...")
        self.assertEqual("ping", fizz_buzz.fizz_buzz(7).split()[-1].lower())

    def test_pong(self):
        print("Testing Pong ...")
        self.assertEqual("pong", fizz_buzz.fizz_buzz(11).split()[-1].lower())

    def test_all(self):
        print("Testing 1155 ...")
        self.assertEqual("fizzbuzzpingpong", fizz_buzz.fizz_buzz(1155).split()[-1].lower())

