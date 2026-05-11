import unittest
import scientic_calculator.core as core


class TestAdd(unittest.TestCase):

    def setUP(self):
        self.core = core.Core()

    def test_add_positive_numbers(self):
        result = core.add(-4, -7)
        self.assertEqual(result, -11)


if __name__ == "__main__":
    unittest.main()