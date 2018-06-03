from abc import abstractmethod, ABCMeta
from .utils import CustomFloat


class LookupTable(object):
    __metaclass__ = ABCMeta

    def __init__(self, k):
        self.k = k

    @abstractmethod
    def __getitem__(self, item):
        pass


class F31(LookupTable):

    def __getitem__(self, yk):
        result = yk ** 2 - 2 ** (-2 * self.k)
        return CustomFloat.from_float(result)


class F32(LookupTable):

    def __getitem__(self, t):
        result = t ** 2 * 2 ** (-2 * self.k)
        return CustomFloat.from_float(result)


class F4(LookupTable):

    def __getitem__(self, yk):
        result = 1 / (yk ** 4 - yk ** 2 * 2 ** (-2 * self.k) + 2 ** -(4 * self.k + 3))
        return CustomFloat.from_float(result)
