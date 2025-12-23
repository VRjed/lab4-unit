import unittest
from rectangle import area, perimeter


class RectangleTestCase(unittest.TestCase):

    def test_area_zero(self):
        self.assertEqual(area(10, 0), 0)

    def test_area_square(self):
        self.assertEqual(area(5, 5), 25)

    def test_area_rectangle(self):
        self.assertEqual(area(3, 4), 12)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(10, 0), 20)

    def test_perimeter_square(self):
        self.assertEqual(perimeter(5, 5), 20)

    def test_perimeter_rectangle(self):
        self.assertEqual(perimeter(3, 4), 14)


if __name__ == "__main__":
    unittest.main()
