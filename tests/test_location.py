import unittest
from modules.location import get_location

class TestLocation(unittest.TestCase):
    def test_get_location(self):
        location = get_location()
        self.assertIn('city', location)
        self.assertIn('country', location)

if __name__ == '__main__':
    unittest.main()
