from logic_utils import check_guess, parse_guess, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


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


# --- check_guess: swapped hint message bug fix ---

def test_too_high_hint_says_go_lower():
    # Previously returned "Go HIGHER!" when guess was too high — messages were swapped
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"

def test_too_low_hint_says_go_higher():
    # Previously returned "Go LOWER!" when guess was too low — messages were swapped
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"


# --- update_score: off-by-one win score bug fix ---

def test_win_on_attempt_1_scores_90():
    # Previously used (attempt_number + 1), so attempt 1 gave 100 - 10*2 = 80
    # Fixed formula: 100 - 10 * 1 = 90
    score = update_score(0, "Win", 1)
    assert score == 90

def test_win_on_attempt_5_scores_50():
    # Sanity check: 100 - 10 * 5 = 50, floored at 10
    score = update_score(0, "Win", 5)
    assert score == 50


# --- update_score: "Too High" awarding points bug fix ---

def test_too_high_on_even_attempt_deducts_points():
    # Previously awarded +5 on even attempts; now always deducts 5
    score = update_score(50, "Too High", 2)
    assert score == 45

def test_too_high_and_too_low_deduct_equally():
    # Both wrong-guess outcomes should behave the same
    score_high = update_score(50, "Too High", 2)
    score_low = update_score(50, "Too Low", 2)
    assert score_high == score_low
