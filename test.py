import unittest
import main

class TestMain(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main.main(), "Hello, World!")

if __name__ == '__main__':
    unittest.main()
