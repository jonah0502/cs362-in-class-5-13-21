import unittest
import program1 as code

class TestCase(unittest.TestCase):

    def test_1(self):
        self.assertEqual(code.isPal("ollo"), True)
    def test_2(self):
        self.assertEqual(code.isPal("hello"), False)
    @unittest.expectedFailure
    def test_3(self):
        self.assertEqual(code.isPal("yoinks"), True)



if __name__ == "__main__":
    unittest.main(verbosity=2)