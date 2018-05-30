from .tables import F31, F32, F4
from .utils import partition, CustomFloat


class MultiplicativeDivider:

    def __init__(self, x, y, k=5, p=10):
        self.x = x
        self.k = k
        self.p = p
        self.yk, self.t = partition(y.fraction, k)
        self.f31_table = F31(k)
        self.f32_table = F32(k)
        self.f4_table = F4(k)

    def divide(self):
        return self.f1 * self.f2 * self.f3 * self.f4

    @property
    def f1(self):
        return self.x

    @property
    def f2(self):
        t = CustomFloat(self.t.whole, self.t.fraction >> self.k)
        return self.yk - t

    @property
    def f3(self):
        return self.f31_table[float(self.yk)] + self.f32_table[float(self.t)]

    @property
    def f4(self):
        return self.f4_table[float(self.yk)]
