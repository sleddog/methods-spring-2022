import unittest
import fizzbuzz

class TestFizzBuzz(unittest.TestCase):
    def test_fizz(self):
        res = fizzbuzz.fizzBuzz(3)
        self.assertEqual(res, "Fizz")

    def test_buzz(self):
        res = fizzbuzz.fizzBuzz(5)
        self.assertEqual(res, "Buzz")

    def test_fizzbuzz(self):
        res = fizzbuzz.fizzBuzz(15)
        self.assertEqual(res, "FizzBuzz")

    def test_ping(self):
        res = fizzbuzz.fizzBuzz(7)
        self.assertEqual(res, "Ping")

    def test_pong(self):
        res = fizzbuzz.fizzBuzz(11)
        self.assertEqual(res, "Pong")

    def test_pingpong(self):
        res = fizzbuzz.fizzBuzz(77)
        self.assertEqual(res, "PingPong")

    def test_fizzbuzzpingpong(self):
        res = fizzbuzz.fizzBuzz(1155)
        self.assertEqual(res, "FizzBuzzPingPong")
