import unittest

from fizzbuzz import fizzbuzz


class FizzBuzzTests(unittest.TestCase):

    def call_fizz_buzz(self, n_integer: int) -> str:
        return fizzbuzz(n_integer).lower().split('\n')[-2]

    def test_fizz(self) -> None:
        self.assertEqual(self.call_fizz_buzz(3), "fizz")

    def test_buzz(self) -> None:
        self.assertEqual(self.call_fizz_buzz(5), "buzz")

    def test_ping(self) -> None:
        self.assertEqual(self.call_fizz_buzz(7), "ping")

    def test_pong(self) -> None:
        self.assertEqual(self.call_fizz_buzz(11), "pong")

    def test_combination(self) -> None:
        self.assertEqual(self.call_fizz_buzz(1155), "fizzbuzzpingpong")
