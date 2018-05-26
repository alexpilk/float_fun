from .tables import F31, F32, F4
from .utils import decimal_to_bits, bits_to_decimal


class MultiplicativeDivider:

    def __init__(self, x, y, k=5, p=10):
        self.x = x
        self.y = y
        self.k = k
        self.p = p
        self.f31_table = F31(k)
        self.f32_table = F32(k)
        self.f4_table = F4(k)

    def divide(self):
        return self.f1 * self.f2 * self.f3 * self.f4

    @property
    def yk(self):
        whole, fraction = decimal_to_bits(self.y)
        bits = whole + fraction
        bits += [0] * (self.p - len(bits))
        bits = bits_to_decimal([bits[0]], bits[1:self.k])
        return bits + 2 ** -self.k

    @property
    def t(self):
        whole, fraction = decimal_to_bits(self.y)
        bits = whole + fraction
        bits += [0] * (self.p - len(bits))
        bits = bits[self.k:]
        return bits_to_decimal([bits[0]], bits[1:]) - 1

    @property
    def f1(self):
        return self.x

    @property
    def f2(self):
        return self.yk - self.t * 2 ** -self.k

    @property
    def f3(self):
        return self.f31_table[self.yk] + self.f32_table[self.t]

    @property
    def f4(self):
        return self.f4_table[self.yk]
