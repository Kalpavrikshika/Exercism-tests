import unittest

from hello_world import helo_world

# Tests adapted from `problem-specifications//canonical-data.json` @ v1.1.0

class HelloWorldTests(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(helo_world(),"Hello, World!")

if __name__ == '__main__':
    unittest.main()
