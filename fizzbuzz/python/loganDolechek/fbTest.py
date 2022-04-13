from fizzBuzz import fizzbuzz

def test_1_is_1():
     assertEqual(FizzBuzz(1), 1)

def test_8_is_8():
     assertEqual(FizzBuzz(8), 8)

def test_Fizz_For3():
     assertEqual(FizzBuzz(1), "Fizz")

def test_Buzz_For5():
     assertEqual(FizzBuzz(5), "Buzz")

def test_Ping_For7():
     assertEqual(FizzBuzz(7), "Ping")

def test_Pong_For11():
     assertEqual(FizzBuzz(11), "Pong")

def test_FizzBuzz_For15():
     assertEqual(FizzBuzz(15), "FizzBuzz")

def test_FizzPing_For21():
     assertEqual(FizzBuzz(21), "FizzPing")

def test_FizzPong_For33():
     assertEqual(FizzBuzz(33), "FizzPong")

def test_BuzzPing_For35():
     assertEqual(FizzBuzz(35), "BuzzPing")

def test_BuzzPong_For55():
     assertEqual(FizzBuzz(55), "BuzzPong")

def test_BuzzPingPong_For385():
     assertEqual(FizzBuzz(385), "BuzzPingPong")

def test_FizzBuzzPing_For105():
     assertEqual(FizzBuzz(105), "FizzBuzzPing")

def test_FizzBuzzPingPong_For1155():
     assertEqual(FizzBuzz(1155), "FizzBuzzPingPong")
