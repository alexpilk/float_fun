import logging

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)


def normalize(number, max_bits=8):
    if not number:
        return number

    if number > 2 ** max_bits:
        raise OverflowError('Number {} doesn\'t fit on {} bits!'.format(number, max_bits))

    mask = 1 << max_bits - 1
    while not (number & mask):
        number <<= 1

    return number


class Float:

    def __init__(self, whole, fraction, resolution=8):
        self.whole = whole
        self.fraction = fraction
        self.resolution = resolution

    @property
    def positive(self):
        return True if self.whole >= 0 and self.fraction >= 0 else False

    def __repr__(self):
        fraction_repr = '{:b}'.format(abs(self.fraction))
        fraction_repr = '0' * (self.resolution - len(fraction_repr)) + fraction_repr
        return '{sign}{whole:b}.{fraction}'.format(
            sign='+' if self.positive else '-',
            whole=abs(self.whole),
            fraction=fraction_repr)


def partition(fraction, partition_index):
    fraction = normalize(fraction)
    mask = normalize(2 ** (partition_index - 1) - 1)
    yk_whole = 1
    yk_fraction = (fraction & mask) + (normalize(1) >> (partition_index - 1))
    yk = Float(yk_whole, yk_fraction)
    t_mask = (normalize(1) - 1 << 1) - mask + 1
    t_raw = ((fraction & t_mask) << (partition_index - 1)) - normalize(1)
    t = Float(0, t_raw << 1)
    logger.info('Fraction 1.{fraction:b} partitioned: yk {yk}, t {t}'.format(fraction=fraction, yk=yk, t=t))
    return yk, t


if __name__ == '__main__':
    x = Float(2, 11)
    y = Float(1, 5)

    print(y)

    yk, t = partition(y.fraction, 3)
    print(yk, t)
    # print(bin(yk * t))
