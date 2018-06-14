import logging
from multiplicative_divider import MultiplicativeDivider, CustomFloat


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler('loop32.txt')
file_handler.setLevel(logging.INFO)
logger.addHandler(file_handler)


def test_division(x, y):
    expected_result = CustomFloat.from_float(x / y)
    x = CustomFloat.from_float(x)
    y = CustomFloat.from_float(y)
    divider = MultiplicativeDivider(x, y, k=12)
    result = divider.divide()
    error = len('{:b}'.format(result.fraction ^ expected_result.fraction))
    logger.info('{x:f}\t{y:f}\t{result:f}\t{expected_result:f}\t{result}\t{expected_result}\t{error}'.format(
        x=x, y=y, result=result, expected_result=expected_result, error=error
    ))


if __name__ == '__main__':
    logger.info('x\ty\tdivider_dec\treal_dec\tdivider_bin\treal_bin\terror')
    input_y = 1.0
    step = 0.01
    while input_y < 2:
        input_x = input_y
        limit = input_y * 1.9999
        while input_x < limit:
            test_division(input_x, input_y)
            input_x += step
        input_y += step
