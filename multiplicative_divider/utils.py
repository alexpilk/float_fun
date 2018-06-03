from .resolution import DEFAULT_RESOLUTION
from .custom_float import CustomFloat
import logging

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)


def normalize(number, max_bits=DEFAULT_RESOLUTION):
    if not number:
        return number

    if number > 2 ** max_bits:
        raise OverflowError('Number {} doesn\'t fit on {} bits!'.format(number, max_bits))

    mask = 1 << max_bits - 1
    while not (number & mask):
        number <<= 1

    return number


def partition(fraction, partition_index):
    #fraction = normalize(fraction)
    mask = normalize(2 ** (partition_index - 1) - 1)
    yk_whole = 1
    yk_fraction = (fraction & mask) + (normalize(1) >> (partition_index - 1))
    yk = CustomFloat(yk_whole, yk_fraction)
    t_mask = (normalize(1) - 1 << 1) - mask + 1
    t_raw = ((fraction & t_mask) << (partition_index - 1)) - normalize(1)
    t = CustomFloat(0, t_raw << 1)
    logger.info('Fraction 1.{fraction:b} partitioned: yk {yk}, t {t}'.format(fraction=fraction, yk=yk, t=t))
    return yk, t
