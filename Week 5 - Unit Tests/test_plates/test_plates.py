from plates import is_valid

def test_letters_after_numbers():
    assert is_valid('ab23a5') == False

def test_first_letters():
    assert is_valid('0ab232') == False
    assert is_valid('a02356') == False
    assert is_valid('ab2345') == True
    assert is_valid('12345') == False

def test_under():
    assert is_valid('a') == False

def test_over():
    assert is_valid('asd2356')==False

def test_zero_placement():
    assert is_valid('asd032') == False

def test_alphanumeric():
    assert is_valid('ab@%#')== False