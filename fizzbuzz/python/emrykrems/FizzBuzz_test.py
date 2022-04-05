from FizzBuzz import FizzBuzz

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

def test_FizzBuzzPing_For105():
    assert FizzBuzz(105) == "FizzBuzzPing"

def test_FizzBuzzPingPong_For1155():
    assert FizzBuzz(1155) == "FizzBuzzPingPong"
