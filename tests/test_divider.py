from multiplicative_divider import MultiplicativeDivider, CustomFloat
import unittest
import logging


logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)


def divide(x, y, k=5):
    x = CustomFloat.from_float(x)
    y = CustomFloat.from_float(y)
    divider = MultiplicativeDivider(x, y, k)
    result = divider.divide()
    return float(result)


class TestDivider(unittest.TestCase):

    def test_regular(self):
        result = divide(2.1992187, 1.5390625)
        self.assertAlmostEqual(result, 1.4289339776649745, places=5)

    def test_small_num_small_diff(self):
        result = divide(1.01, 1)
        self.assertAlmostEqual(result, 1.01, places=6)

    def test_small_num_big_diff(self):
        result = divide(2.01, 1.01)
        self.assertAlmostEqual(result, 1.9900990099009899, places=6)

    def test_big_num_small_diff(self):
        result = divide(2, 1.99)
        self.assertAlmostEqual(result, 1.0050251256281406, places=5)

    def test_big_num_big_diff(self):
        result = divide(3.7, 1.99)
        self.assertAlmostEqual(result, 1.8592964824120604, places=5)


if __name__ == '__main__':
    unittest.main()
