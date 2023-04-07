import unittest
from Stamp_Duty import StampDuty

class TestStampDuty(unittest.TestCase):
    def test_calculate_tax(self):
        tax_calculator = StampDuty()
        self.assertEqual(78350, StampDuty.calculate_tax_percent(1000000))

    def test_calculate_tax2(self):
        tax_calculator = StampDuty()
        self.assertEqual(1840, StampDuty.calculate_tax_percent(237000))

    def test_calculate_tax3(self):
        tax_calculator = StampDuty()
        self.assertEqual(0, StampDuty.calculate_tax_percent(140000))

    def test_calculate_tax4(self):
        tax_calculator = StampDuty()
        self.assertEqual(8850, StampDuty.calculate_tax_percent(355000))

    def test_calculate_tax5(self):
        tax_calculator = StampDuty()
        self.assertEqual(790, StampDuty.calculate_tax_percent(184500))

    def test_calculate_tax6(self):
        tax_calculator = StampDuty()
        self.assertEqual(48350, StampDuty.calculate_tax_percent(750001))

    def test_calculate_tax7(self):
        tax_calculator = StampDuty()
        self.assertEqual(0, StampDuty.calculate_tax_percent(True))

    def test_calculate_tax8(self):
        tax_calculator = StampDuty()
        self.assertEqual('Invalid type', StampDuty.calculate_tax_percent('True'))


if __name__ == '__main__':
    unittest.main()