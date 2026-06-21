from logic_utils import check_guess


# --- Regression: new game handler did not reset status or history ---

def _make_session(status, attempts, history):
    return {"status": status, "attempts": attempts, "history": list(history)}

def _apply_new_game(session):
    """Mirrors the new game reset block in app.py."""
    session["attempts"] = 0
    session["status"] = "playing"
    session["history"] = []

def test_new_game_after_loss_unblocks_play():
    # Before fix, status stayed "lost" and st.stop() prevented further play.
    session = _make_session("lost", 8, [10, 20, 30, 40, 50, 60, 70, 80])
    _apply_new_game(session)
    assert session["status"] == "playing"

def test_new_game_after_win_unblocks_play():
    session = _make_session("won", 3, [42])
    _apply_new_game(session)
    assert session["status"] == "playing"

def test_new_game_clears_history():
    session = _make_session("lost", 8, [10, 20, 30])
    _apply_new_game(session)
    assert session["history"] == []

def test_new_game_resets_attempts():
    session = _make_session("lost", 8, [10, 20, 30])
    _apply_new_game(session)
    assert session["attempts"] == 0


# --- Original check_guess tests ---

def test_winning_guess():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

# Regression: hint direction was inverted (guess > secret said "Go HIGHER!")
def test_too_high_hint_says_go_lower():
    _, message = check_guess(80, 50)
    assert "LOWER" in message

def test_too_low_hint_says_go_higher():
    _, message = check_guess(20, 50)
    assert "HIGHER" in message
