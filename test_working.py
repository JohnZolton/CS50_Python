from working import convert
import pytest

def test_good_input():
    assert convert('9:00 AM to 5:00 PM') == '09:00 to 17:00'
    assert convert('9 AM to 5 PM') == '09:00 to 17:00'
    assert convert('10:30 PM to 8:50 AM') == '22:30 to 08:50'


def test_bad_input():
    # check hours
    with pytest.raises(ValueError):
        convert('13:00 AM to 15:00 PM')
    # check minutes
    with pytest.raises(ValueError):
        convert('9:60 AM to 5:60 PM')
    #check format
    with pytest.raises(ValueError):
        convert('9 AM - 9 PM')
    with pytest.raises(ValueError):
        convert('9AM to 10PM')
    with pytest.raises(ValueError):
        convert('9 to 10')


