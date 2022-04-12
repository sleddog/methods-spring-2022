import sys
from typing import Dict


def fizzbuzz(n: int):

    fizz_buzz_dict: Dict[int, str] = {3: "Fizz",
                                      5: "Buzz",
                                      7: "Ping",
                                      11: "Pong"}

    for num in range(1, n + 1):
        print_string: str = ""
        for int_key in fizz_buzz_dict.keys():
            print_string += fizz_buzz_dict[int_key]
        if print_string == "":
            print_string = str(num)
        print(print_string)


def main(number: int):
    fizzbuzz(number)


# Run main using the command line argument
if __name__ == "__main__":
    main(int(sys.argv[1]))
