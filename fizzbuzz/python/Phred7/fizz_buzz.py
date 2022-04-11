###############################
# For CSCI455 Industry Methods at Montana State University in Spring 2022.
# Written by Walker Ward aka Phred7
###############################

import re
import sys
from typing import Dict
import unittest


def fizz_buzz(integer: int) -> str:
    """
    Solves the fizzbuzz problem.
    The local dictionary `fizz_buzz_dict: Dict[int, str] = {3: "Fizz", 5: "Buzz"}` may be modified to add or remove
    support for more values that replace actual integer value in the return string. Each key in this dictionary is
    modded with each number in (0, input] if the result is 0 then the value of the key in this dict is appended to the
    str returned by this function.
    :param integer: An integer greater than or equal to 1.
    :return: str representation of this fizzbuzz solution.
    """
    fizz_buzz_dict: Dict[int, str] = {3: "Fizz",
                                      5: "Buzz",
                                      7: "Ping",
                                      11: "Pong"}
    return_str: str = ""
    for value in range(1, integer+1):
        value_str: str = ""
        for key in fizz_buzz_dict.keys():
            if value % key == 0:
                value_str += fizz_buzz_dict.get(key)
        if value_str == "":
            value_str += str(value)
        return_str += f"{value_str}\n"
    return return_str

if __name__ == "__main__":
    if len(sys.argv) > 1:   # verifies that there is more than one command line argument. We want the second argument.
        command_line_argument: str = sys.argv[1]
        if re.match("[-+]?\d*[.]?\d+$", command_line_argument) is not None:  # verifies that command_line_argument is a number using a regex.
            first_command_line_argument_integer: int = int(float(command_line_argument))  # convert to an int.
            if first_command_line_argument_integer > 0:
                print(fizz_buzz(first_command_line_argument_integer))   # call fizz_buzz solution function and print result.
            else:
                print(f"input parameter \'{sys.argv[1]}\' is not greater than 0")
        else:
            print(f"input parameter \'{sys.argv[1]}\' is not an number")
    else:
        print("missing command line argument")

