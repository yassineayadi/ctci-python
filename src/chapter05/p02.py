

def binary_to_string(val: float):
    array = str(val)
    integers, decimals = ints, decs = array.split(".")
    integers = integers
    exponents = []
    mantissa = []
    digit = integers[0]
    while digit:

        remainder = integers // 2