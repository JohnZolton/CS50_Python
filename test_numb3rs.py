from numb3rs import validate

def test_good():
    assert validate('1.1.1.1') == True

def test_bad():
    assert validate('1.2.2.256')== False
    assert validate('a.b.b.c') == False
    assert validate('cat') == False