
class PrecisionError(Exception):
    pass

def get_binary_integers(integer: int) -> list:
    exponents = []
    while integer:
        quotient, exp = integer // 2, integer % 2
        exponents.append(exp)
        integer = quotient
    return exponents[::-1]


def get_biased_form(exponent: int) -> list:
    bias = get_binary_integers(127 + exponent)
    return right_pad(bias, 8)


def get_binary_decimals(fraction: float) -> list:
    mantissa = []
    while fraction and len(mantissa) < 23:
        fraction = fraction * 2
        decimal = int(fraction)
        mantissa.append(decimal)
        fraction = fraction - decimal

    if fraction:
        raise PrecisionError(
            "Insufficient precision, cannot represent value in binary format."
        )
    return mantissa


def get_exponent(integers, mantissa):
    if integers and integers[0] == 1:
        exp = len(integers) - 1
    else:
        exp = -1
        for v in mantissa:
            if v == 0:
                exp -= 1
            else:
                break
    return exp


def left_pad(arr: list, size: int):
    while len(arr) < size:
        arr = arr + [0]
    return arr


def right_pad(arr: list, size: int):
    while len(arr) < size:
        arr = [0] + arr
    return arr


def get_significand(integers: list, decimals: list, exponent: int):
    mantissa = integers + decimals
    if exponent < 0:
        significand = mantissa[abs(exponent):]
    else:
        significand = mantissa[1:]
    return left_pad(significand, 23)


def float_to_binary_form(float_number: float):
    sign = [1] if float_number < 0 else [0]
    integers, decimals = int(float_number), abs(float_number - int(float_number))
    integers = get_binary_integers(integers)
    decimals = get_binary_decimals(decimals)
    exponent = get_exponent(integers, decimals)
    significand = get_significand(integers, decimals,exponent)
    exponent = get_biased_form(exponent)
    binary_form = sign + exponent + significand
    print(binary_form)
    return "".join(str(d) for d in binary_form)
