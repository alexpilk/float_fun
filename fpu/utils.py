import logging

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)


def normalize(number, max_bits=24):
    if not number:
        return number

    if number > 2 ** max_bits:
        raise OverflowError('Number {} doesn\'t fit on {} bits!'.format(number, max_bits))

    mask = 1 << max_bits - 1
    while not (number & mask):
        number <<= 1

    return number


class CustomFloat:

    default_resolution = 24

    def __init__(self, whole, fraction, resolution=default_resolution):
        self.whole = whole
        self.fraction = fraction
        self.resolution = resolution

    @classmethod
    def from_float(cls, number, resolution=default_resolution):
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


def partition(fraction, partition_index):
    fraction = normalize(fraction)
    mask = normalize(2 ** (partition_index - 1) - 1)
    yk_whole = 1
    yk_fraction = (fraction & mask) + (normalize(1) >> (partition_index - 1))
    yk = CustomFloat(yk_whole, yk_fraction)
    t_mask = (normalize(1) - 1 << 1) - mask + 1
    t_raw = ((fraction & t_mask) << (partition_index - 1)) - normalize(1)
    t = CustomFloat(0, t_raw << 1)
    logger.info('Fraction 1.{fraction:b} partitioned: yk {yk}, t {t}'.format(fraction=fraction, yk=yk, t=t))
    return yk, t
