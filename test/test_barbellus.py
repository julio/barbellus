import unittest
from barbellus.barbellus import Barbellus
from barbellus.exceptions import InvalidWeight

class TestBarbellus(unittest.TestCase):
    def setUp(self):
        self.plates_available = [1, 5, 10, 25, 35, 45]

    def test_empty_bar(self):
        weight_to_lift = 45

        barbellus = Barbellus(self.plates_available, weight_to_lift)
        plates = barbellus.build_plate_rack().select_plates()

        self.assertEqual([], plates)

    def test_less_than_bar(self):
        weight_to_lift = 35
        self.assertRaises(InvalidWeight, Barbellus, self.plates_available, weight_to_lift)

    def test_65(self):
        weight_to_lift = 65

        barbellus = Barbellus(self.plates_available, weight_to_lift)
        plates = barbellus.build_plate_rack().select_plates()

        self.assertEqual([10], plates)

    def test_47(self):
        weight_to_lift = 47

        barbellus = Barbellus(self.plates_available, weight_to_lift)
        plates = barbellus.build_plate_rack().select_plates()

        self.assertEqual([1], plates)

    def test_67(self):
        weight_to_lift = 67

        barbellus = Barbellus(self.plates_available, weight_to_lift)
        plates = barbellus.build_plate_rack().select_plates()

        self.assertEqual([10, 1], plates)

    @unittest.SkipTest
    def test_69(self):
        weight_to_lift = 69

        barbellus = Barbellus(self.plates_available, weight_to_lift)
        plates = barbellus.build_plate_rack().select_plates()
        barbellus.debug()
        self.assertEqual([10, 2], plates)

    @unittest.SkipTest
    def test_75(self):
        weight_to_lift = 75

        barbellus = Barbellus(self.plates_available, weight_to_lift)
        plates = barbellus.build_plate_rack().select_plates()
        barbellus.debug()
        self.assertEqual([10, 5], plates)

    def test_95(self):
        weight_to_lift = 95

        barbellus = Barbellus(self.plates_available, weight_to_lift)
        plates = barbellus.build_plate_rack().select_plates()

        self.assertEqual([25], plates)


    def test_135(self):
        weight_to_lift = 135

        barbellus = Barbellus(self.plates_available, weight_to_lift)
        plates = barbellus.build_plate_rack().select_plates()

        self.assertEqual([45], plates)

    def test_225(self):
        weight_to_lift = 225

        barbellus = Barbellus(self.plates_available, weight_to_lift)
        plates = barbellus.build_plate_rack().select_plates()

        self.assertEqual([45, 45], plates)

    def test_185(self):
        weight_to_lift = 185

        barbellus = Barbellus(self.plates_available, weight_to_lift)
        plates = barbellus.build_plate_rack().select_plates()

        self.assertEqual([45, 25], plates)


if __name__ == '__main__':
    unittest.main()
