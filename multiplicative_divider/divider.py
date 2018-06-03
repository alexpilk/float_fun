from .tables import F31, F32, F4
from .utils import partition, CustomFloat


class MultiplicativeDivider:

    def __init__(self, x, y, k=5):
        """
        :param CustomFloat x: dividend
        :param CustomFloat y: divisor
        :param int k: partitioning index
        """
        if not 1 <= float(y) < 2:
            raise ValueError('Y should satisfy 1 <= y < 2')
        if not float(x) >= float(y) or not float(x) < 2 * float(y):
            raise ValueError('X/Y should satisfy 1 <= X/Y < 2')
        self.x = x
        self.k = k
        self.yk, self.t = partition(y.fraction, k)
        self.f31_table = F31(k)
        self.f32_table = F32(k)
        self.f4_table = F4(k)

    def divide(self):
        """
        :return: product of 4 factors
        :rtype: CustomFloat
        """
        return self.f1 * self.f2 * self.f3 * self.f4

    @property
    def f1(self):
        """
        :return: 1st factor (x)
        :rtype: CustomFloat
        """
        return self.x

    @property
    def f2(self):
        """
        :return: 2nd factor (yk - t * 2^-k)
        :rtype: CustomFloat
        """
        t = CustomFloat(self.t.whole, self.t.fraction >> self.k)
        return self.yk - t

    @property
    def f3(self):
        """
        :return: 3rd factor calculated by table lookup
        :rtype: CustomFloat
        """
        return self.f31_table[float(self.yk)] + self.f32_table[float(self.t)]

    @property
    def f4(self):
        """
        :return: 4th factor calculated by table lookup
        :rtype: CustomFloat
        """
        return self.f4_table[float(self.yk)]

    def __repr__(self):
        return 'x:  {x:f}\t{x}\n' \
               'yk: {yk:f}\t{yk}\n' \
               't:  {t:f}\t{t}\n' \
               'F1: {f1:f}\t{f1}\n' \
               'F2: {f2:f}\t{f2}\n' \
               'F3: {f3:f}\t{f3}\n' \
               'F4: {f4:f}\t{f4}\n'.format(x=self.x, yk=self.yk, t=self.t, f1=self.f1,
                                           f2=self.f2, f3=self.f3, f4=self.f4)
