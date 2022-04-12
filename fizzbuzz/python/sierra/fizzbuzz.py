import sys
from typing import Dict


def fizzbuzz(n: int):
    return_string: str = ""
    fizz_buzz_dict: Dict[int, str] = {3: "Fizz",
                                      5: "Buzz",
                                      7: "Ping",
                                      11: "Pong"}
    for num in range(1, n + 1):
        num_string: str = ""
        for key_int in fizz_buzz_dict.keys():
            if num % key_int == 0:
                num_string += fizz_buzz_dict[key_int]
        if num_string == "":
            num_string = str(num)
        return_string += f"{num_string}\n"
    return return_string


def main(number: int):
    print(fizzbuzz(number))


# Run main using the command line argument
if __name__ == "__main__":
    main(int(sys.argv[1]))
