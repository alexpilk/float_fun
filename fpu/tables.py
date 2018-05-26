from abc import abstractmethod, ABCMeta


class LookupTable(object):
    __metaclass__ = ABCMeta

    def __init__(self, k):
        self.k = k

    @abstractmethod
    def __getitem__(self, item):
        pass


class F31(LookupTable):

    def __getitem__(self, yk):
        return yk ** 2 - 2 ** (-2 * self.k)


class F32(LookupTable):

    def __getitem__(self, t):
        return t ** 2 * 2 ** (-2 * self.k)


class F4(LookupTable):

    def __getitem__(self, yk):
        return 1 / (yk ** 4 - yk ** 2 * 2 ** (-2 * self.k) + 2 ** -(4 * self.k + 3))
