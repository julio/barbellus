from barbellus import Barbellus
import unittest

class BarbellusTest(unittest.TestCase):
    def test_65(self):
        weight_to_lift = 65
        plates_available = [1, 5, 10, 25, 35, 45]

        barbellus = Barbellus(plates_available, weight_to_lift)
        plates = barbellus.build_rack().select_plates()

        self.assertEqual([10], plates)

if __name__ == '__main__':
    unittest.main()
