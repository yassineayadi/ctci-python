from chapter05.p07 import clear_odds, clear_pairs, swap_odds_and_pairs


def test_clear_odds_with_only_odds(odds):
    assert clear_odds(odds) == 0


def test_clear_odds_with_only_pairs(pairs):
    assert clear_odds(pairs) == pairs


def test_clear_pairs_with_only_pairs(pairs):
    assert clear_pairs(pairs) == 0


def test_clear_pairs_with_only_odds(odds):
    assert clear_pairs(odds) == odds


def test_swap_odds_and_pairs():
    number = 0b01010001
    expected = 0b10100010
    assert swap_odds_and_pairs(number) == expected
