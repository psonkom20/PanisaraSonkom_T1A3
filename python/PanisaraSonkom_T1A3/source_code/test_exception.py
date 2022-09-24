from main import get_int

inputs = iter([8, 10])

def fake_input(prompt):
    '''input for testing'''
    return next(inputs)

class TestGetInt:
    '''testing get_int'''
    def test_valid(self, monkeypatch):
        '''test valid input'''
        monkeypatch.setattr('builtins.input', fake_input)
        assert get_int() == 8
        assert get_int() == 10
