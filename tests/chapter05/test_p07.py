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
    input_number = 0b011010
    expected_number = 0b100101
    assert swap_odds_and_pairs(input_number) == expected_number
