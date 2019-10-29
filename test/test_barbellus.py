import unittest
from barbellus.barbellus import Barbellus
from barbellus.exceptions import InvalidWeight

class TestBarbellus(unittest.TestCase):
    def setUp(self):
        self.plates_available = [1, 5, 10, 25, 35, 45]

    def test_less_than_bar(self):
        weight_to_lift = 35
        self.assertRaises(InvalidWeight, Barbellus, self.plates_available, weight_to_lift)

    def test_empty_bar(self):
        self.assertEqual([], self.__plates(45))

    def test_47(self):
        self.assertEqual([1], self.__plates(47))

    def test_65(self):
        self.assertEqual([10], self.__plates(65))

    def test_67(self):
        self.assertEqual([10, 1], self.__plates(67))

    def test_69(self):
        self.assertEqual([10, 1, 1], self.__plates(69))

    def test_75(self):
        self.assertEqual([10, 5], self.__plates(75))

    def test_95(self):
        self.assertEqual([25], self.__plates(95))

    def test_115(self):
        self.assertEqual([35], self.__plates(115))

    def test_135(self):
        self.assertEqual([45], self.__plates(135))

    def test_185(self):
        self.assertEqual([45, 25], self.__plates(185))

    def test_225(self):
        self.assertEqual([45, 45], self.__plates(225))

    def __plates(self, weight_to_lift):
        barbellus = Barbellus(self.plates_available, weight_to_lift)
        return barbellus.build_plate_rack().select_plates()



if __name__ == '__main__':
    unittest.main() # pragma: no cover
