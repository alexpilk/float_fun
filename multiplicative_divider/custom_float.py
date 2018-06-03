from .resolution import DEFAULT_RESOLUTION


class CustomFloat:

    def __init__(self, whole, fraction, resolution=DEFAULT_RESOLUTION):
        self.whole = whole
        self.fraction = fraction
        self.resolution = resolution

    @classmethod
    def from_float(cls, number, resolution=DEFAULT_RESOLUTION):
        whole = int(number // 1)
        fraction = int((number - whole) * 2 ** resolution)
        resolution = resolution
        return cls(whole, fraction, resolution)

    @property
    def positive(self):
        return True if self.whole >= 0 and self.fraction >= 0 else False

    def __sub__(self, other):
        whole = self.whole - other.whole
        fraction = self.fraction - other.fraction
        return CustomFloat(whole, fraction)

    def __add__(self, other):
        whole = self.whole + other.whole
        fraction = self.fraction + other.fraction
        return CustomFloat(whole, fraction)

    def __mul__(self, other):
        num1 = (self.whole << self.resolution) + self.fraction
        num2 = (other.whole << self.resolution) + other.fraction
        result = num1 * num2
        whole = result >> self.resolution * 2
        fraction = result - (whole << self.resolution * 2) >> self.resolution
        return CustomFloat(whole, fraction)

    def __repr__(self):
        fraction_repr = '{:b}'.format(abs(self.fraction))
        fraction_repr = '0' * (self.resolution - len(fraction_repr)) + fraction_repr
        return '{sign}{whole:b}.{fraction}'.format(
            sign='+' if self.positive else '-',
            whole=abs(self.whole),
            fraction=fraction_repr)

    def __format__(self, format_spec):
        if format_spec == 'f':
            return repr(float(self))
        return super(CustomFloat, self).__format__(format_spec)

    def __float__(self):
        return self.whole + (self.fraction / 2 ** self.resolution)
