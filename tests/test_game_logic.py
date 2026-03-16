from logic_utils import check_guess, parse_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


# --- parse_guess: float bug fix ---

def test_float_input_is_rejected():
    # Previously "3.7" was silently truncated to 3; now it should be an error
    ok, value, err = parse_guess("3.7")
    assert ok is False
    assert value is None
    assert err == "Enter a whole number."

def test_whole_number_string_with_no_decimal_is_accepted():
    # Ensure a plain integer string still works after the float fix
    ok, value, err = parse_guess("42")
    assert ok is True
    assert value == 42
    assert err is None


# --- parse_guess: range validation bug fix ---

def test_zero_is_out_of_range():
    # 0 is below the valid range of 1–100
    ok, value, err = parse_guess("0")
    assert ok is False
    assert value is None
    assert err == "Guess must be between 1 and 100."

def test_above_max_is_out_of_range():
    # 101 exceeds the valid range of 1–100
    ok, value, err = parse_guess("101")
    assert ok is False
    assert value is None
    assert err == "Guess must be between 1 and 100."

def test_boundary_values_are_accepted():
    # 1 and 100 are the inclusive edges of the valid range
    ok_low, val_low, _ = parse_guess("1")
    ok_high, val_high, _ = parse_guess("100")
    assert ok_low is True and val_low == 1
    assert ok_high is True and val_high == 100
