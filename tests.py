from fpu.utils import normalize, partition
import unittest
import logging


logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)


class TestNormalization(unittest.TestCase):

    def test_lower(self):
        max_bits = 5
        number = 0b101
        self.assertEqual(normalize(number, max_bits), 0b10100)

    def test_equal(self):
        max_bits = 5
        number = 0b10100
        self.assertEqual(normalize(number, max_bits), 0b10100)

    def test_bigger(self):
        max_bits = 5
        number = 0b101001
        with self.assertRaises(OverflowError):
            normalize(number, max_bits)


class TestPartitioning(unittest.TestCase):

    def test_zero_zero(self):
        fraction = 0b10001
        yk, t = partition(fraction, 4)

        self.assertTrue(yk.positive)
        self.assertEqual(yk.whole, 1)
        self.assertEqual(yk.fraction, normalize(0b1001))

        self.assertFalse(t.positive)
        self.assertEqual(t.whole, 0)
        self.assertEqual(t.fraction, -normalize(1))

    def test_one_one(self):
        fraction = 0b101101
        yk, t = partition(fraction, 4)

        self.assertTrue(yk.positive)
        self.assertEqual(yk.whole, 1)
        self.assertEqual(yk.fraction, normalize(0b1011))

        self.assertTrue(t.positive)
        self.assertEqual(t.whole, 0)
        self.assertEqual(t.fraction, normalize(1) >> 1)

    def test_one_zero(self):
        fraction = 0b101001
        yk, t = partition(fraction, 4)

        self.assertTrue(yk.positive)
        self.assertEqual(yk.whole, 1)
        self.assertEqual(yk.fraction, normalize(0b1011))

        self.assertFalse(t.positive)
        self.assertEqual(t.whole, 0)
        self.assertEqual(t.fraction, -normalize(0b11))

    def test_zero_one(self):
        fraction = 0b100101
        yk, t = partition(fraction, 4)

        self.assertTrue(yk.positive)
        self.assertEqual(yk.whole, 1)
        self.assertEqual(yk.fraction, normalize(0b1001))

        self.assertTrue(t.positive)
        self.assertEqual(t.whole, 0)
        self.assertEqual(t.fraction, normalize(1) >> 1)


if __name__ == '__main__':
    unittest.main()
