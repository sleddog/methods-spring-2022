import re
import sys
from typing import Dict


def fizz_buzz(integer: int) -> str:
    """
    Solves the fizzbuzz problem.
    :param integer: An integer greater than or equal to 1.
    :return: str representation of this fizzbuzz solution.
    """
    fizz_buzz_dict: Dict[int, str] = {3: "Fizz",
                                      5: "Buzz"}
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
    if len(sys.argv) > 1:
        first_command_line_argument: str = sys.argv[1]
        if re.match("[-+]?\d*[.]?\d+$", first_command_line_argument) is not None:
            first_command_line_argument_integer: int = int(float(first_command_line_argument))
            if first_command_line_argument_integer > 0:
                print(fizz_buzz(first_command_line_argument_integer))
            else:
                print(f"input parameter \'{sys.argv[1]}\' is not greater than 0")
        else:
            print(f"input parameter \'{sys.argv[1]}\' is not an number")
    else:
        print("missing command line argument")

