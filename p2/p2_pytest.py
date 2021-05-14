import program2 as code


class TestClass:
    def test_one(self):
        assert code.numWords("Hello my name is jonah.") == 5

    def test_two(self):
        assert code.numWords("Bleep blorp I am a computer program.") == 7
