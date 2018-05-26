import math


def decimal_to_bits(number, precision=20):
    whole_bits = []
    fraction_bits = []
    ttl = precision
    whole_part = math.floor(number)
    fraction = number - whole_part
    while whole_part:
        next_part = whole_part // 2
        remainder = whole_part / 2 - next_part
        whole_part = next_part
        bit = 1 if remainder else 0
        whole_bits.insert(0, bit)
    while fraction != 1 and ttl:
        fraction = fraction * 2
        bit = 0 if fraction < 1 else 1
        fraction = fraction if fraction <= 1 else fraction - 1
        fraction_bits.append(bit)
        ttl -= 1
    return whole_bits, fraction_bits


def bits_to_decimal(whole, fraction):
    whole_part = 0
    fraction_part = 0
    for i, bit in enumerate(reversed(whole)):
        whole_part += bit * (2 ** i)
    for i, bit in enumerate(fraction):
        fraction_part += bit * (2 ** -(i + 1))
    return whole_part + fraction_part


if __name__ == '__main__':
    # print(decimal_to_bits(2.2))
    print(bits_to_decimal([1, 0], [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1]))
