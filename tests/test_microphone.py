import unittest
from modules.microphone import access_microphone
import os

class TestMicrophone(unittest.TestCase):
    def test_access_microphone(self):
        output_file = 'test_output.wav'
        access_microphone(output_file=output_file)
        self.assertTrue(os.path.exists(output_file))
        os.remove(output_file)

if __name__ == '__main__':
    unittest.main()
