from fbSolution import fizzbuzz

def test_1_is_1():
     assert FizzBuzz(1) == 1

def test_8_is_8():
     assert FizzBuzz(8) == 8

def test_Fizz_For3():
     assert FizzBuzz(3) == "Fizz"

def test_Buzz_For5():
     assert FizzBuzz(5) == "Buzz"

def test_Ping_For7():
     assert FizzBuzz(7) == "Ping"

def test_Pong_For11():
     assert FizzBuzz(11) == "Pong"

def test_FizzBuzz_For15():
     assert FizzBuzz(15) == "FizzBuzz"

def test_FizzPing_For21():
     assert FizzBuzz(21) == "FizzPing"

def test_FizzPong_For33():
     assert FizzBuzz(33) == "FizzPong"

def test_BuzzPing_For35():
     assert FizzBuzz(35) == "BuzzPing"

def test_BuzzPong_For55():
     assert FizzBuzz(55) == "BuzzPong"

def test_BuzzPingPong_For385():
     assert FizzBuzz(385) == "BuzzPingPong"

def test_FizzBuzzPing_For105():
     assert FizzBuzz(105) == "FizzBuzzPing"

def test_FizzBuzzPingPong_For1155():
     assert FizzBuzz(1155) == "FizzBuzzPingPong"
