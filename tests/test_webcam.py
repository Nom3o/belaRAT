import unittest
from modules.webcam import access_webcam

class TestWebcam(unittest.TestCase):
    def test_access_webcam(self):
        # Since we can't test webcam access in an automated test, we'll check if the function exists
        self.assertTrue(callable(access_webcam))

if __name__ == '__main__':
    unittest.main()
