from logic_utils import check_guess, parse_guess, update_score, get_range_for_difficulty

# --- check_guess ---

def test_winning_guess():
    result = check_guess(50, 50)
    assert result == ("Win", "🎉 Correct!")

def test_guess_too_high():
    result = check_guess(60, 50)
    assert result == ("Too High", "📉 Go LOWER!")

def test_guess_too_low():
    result = check_guess(40, 50)
    assert result == ("Too Low", "📈 Go HIGHER!")

def test_guess_boundary_low():
    # Guessing 1 when secret is 1 should win
    result = check_guess(1, 1)
    assert result == ("Win", "🎉 Correct!")

def test_guess_boundary_high():
    # Guessing one above the secret should be Too High
    result = check_guess(101, 100)
    assert result == ("Too High", "📉 Go LOWER!")


# --- parse_guess ---

def test_parse_valid_integer():
    ok, value, err = parse_guess("42")
    assert ok is True
    assert value == 42
    assert err is None

def test_parse_valid_float_truncates():
    # "3.7" should become 3
    ok, value, err = parse_guess("3.7")
    assert ok is True
    assert value == 3
    assert err is None

def test_parse_empty_string():
    ok, value, err = parse_guess("")
    assert ok is False
    assert value is None
    assert err == "Enter a guess."

def test_parse_none():
    ok, value, err = parse_guess(None)
    assert ok is False
    assert value is None
    assert err == "Enter a guess."

def test_parse_non_number():
    ok, value, err = parse_guess("abc")
    assert ok is False
    assert value is None
    assert err == "That is not a number."


# --- update_score ---

def test_score_win_first_attempt():
    # attempt_number=1: points = 100 - 10*(1+1) = 80
    result = update_score(0, "Win", 1)
    assert result == 80

def test_score_win_minimum_points():
    # attempt_number=10: 100 - 10*11 = -10, clamped to 10
    result = update_score(0, "Win", 10)
    assert result == 10

def test_score_win_adds_to_existing():
    result = update_score(50, "Win", 1)
    assert result == 130

def test_score_wrong_guess_deducts():
    result = update_score(50, "Too High", 1)
    assert result == 45

def test_score_too_low_deducts():
    result = update_score(50, "Too Low", 1)
    assert result == 45

def test_score_too_high_always_deducts():
    # Even on even attempt numbers, Too High should still deduct (old bug was +5)
    result = update_score(50, "Too High", 2)
    assert result == 45


# --- get_range_for_difficulty ---

def test_range_easy():
    assert get_range_for_difficulty("Easy") == (1, 20)

def test_range_normal():
    assert get_range_for_difficulty("Normal") == (1, 100)

def test_range_hard():
    _, high = get_range_for_difficulty("Hard")
    # Hard should be harder (wider) than Normal
    assert high > 100

def test_range_hard_is_harder_than_normal():
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high = get_range_for_difficulty("Hard")
    assert hard_high > normal_high

def test_range_unknown_difficulty_defaults():
    assert get_range_for_difficulty("Unknown") == (1, 100)
