from fuel import convert, gauge
import pytest

def main():
    test_zero_division()
    test_value_error()
    test_convert()
    test_gauge()

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert('1/0')

def test_value_error():
    with pytest.raises(ValueError):
        convert('cat/1')

def test_convert():
    assert convert('50/100') == 50
    assert convert('1/100') == 1
    assert convert('99/100')==99

def test_gauge():
    assert gauge(1) == 'E'
    assert gauge(99) == 'F'
    assert gauge(50) == '50%'

if __name__== "__main__":
    main()