from twttr import shorten

def test_twttr():
    assert shorten("aeiouAEIOU") == ''
    assert shorten("Mr. Jock, TV quiz PhD., bags few lynx") == 'Mr. Jck, TV qz PhD., bgs fw lynx'
    assert shorten("1234567890") == "1234567890"