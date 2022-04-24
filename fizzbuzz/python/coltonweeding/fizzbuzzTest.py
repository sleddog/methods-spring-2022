import fizzbuzz
import unittest

fb = fizzbuzz.FizzBuzz()

class fizzbuzzTest(unittest.TestCase):

    def testNumbers(self):
        self.assertEqual(97, fb.FizzBuzz(97), 'Should be 97')
        self.assertEqual(1, fb.FizzBuzz(1), 'Should be 1')
        self.assertEqual(13, fb.FizzBuzz(13), 'Should be 13')

    def testFizz(self):
        self.assertEqual('Fizz', fb.FizzBuzz(6), 'Should be Fizz')

    def testBuzz(self):
        self.assertEqual('Buzz', fb.FizzBuzz(10), 'Should be Buzz')

    def testPing(self):
        self.assertEqual('Ping', fb.FizzBuzz(14), 'Should be Ping')

    def testPong(self):
        self.assertEqual('Pong', fb.FizzBuzz(22), 'Should be Pong')

    def testFizzBuzz(self):
        self.assertEqual('FizzBuzz', fb.FizzBuzz(30), 'Should be FizzBuzz')

    def testPingPong(self):
        self.assertEqual('PingPong', fb.FizzBuzz(77), 'Should be PingPong')

    def testFizzPong(self):
        self.assertEqual('FizzPong', fb.FizzBuzz(33), 'Should be FizzPong')

    def testFizzPing(self):
        self.assertEqual('FizzPing', fb.FizzBuzz(21), 'Should be FizzPing')

    def testBuzzPong(self):
        self.assertEqual('BuzzPong', fb.FizzBuzz(55), 'Should be BuzzPong')

    def testBuzzPing(self):
        self.assertEqual('BuzzPing', fb.FizzBuzz(35), 'Should be BuzzPing')

    def testFizzBuzzPingPong(self):
        self.assertEqual('FizzBuzzPingPong', fb.FizzBuzz(1155), 'Should be FizzBuzzPingPong')

if __name__ == "__main__":
    unittest.main()
