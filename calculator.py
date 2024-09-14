# Description - program calculates basic mathematical operations: +,-,*,/
# Input - user enters numbers and operation sign
# Output - calculated number
# Authors: Калинина, Козлова, Субракова, Финк
inp = input()


def main(inp):
    string_to_list = inp.split(" ")
    a = float(string_to_list[0])
    b = float(string_to_list[2])
    operator = string_to_list[1]
    return a, b, operator

