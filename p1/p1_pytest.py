import program1 as code


class TestClass:
    def test_one(self):
        assert code.isPal("ollo") == True

    def test_two(self):
        assert code.isPal("hello") == False
