import unittest
import program2 as code

class TestCase(unittest.TestCase):

    def test_1(self):
        self.assertEqual(code.numWords("Hello my name is jonah."), 5)
    def test_2(self):
        self.assertEqual(code.numWords("Bleep blorp I am a computer program."), 7)
    @unittest.expectedFailure
    def test_3(self):
        self.assertEqual(code.isPal("yoinks."), 2)



if __name__ == "__main__":
    unittest.main(verbosity=2)