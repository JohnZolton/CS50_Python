from bank import value

def test_bank():
    assert value('sup') == 100
    assert value('hello') == 0
    assert value('hi') == 20
    assert value('Sup') == 100
    assert value('Hello') == 0
    assert value('Hi') == 20