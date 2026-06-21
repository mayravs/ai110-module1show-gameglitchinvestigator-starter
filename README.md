# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- **Purpose of this game:** The purpose of this game is to guess the correct number with a limited amount of attempts.
- **Bug 1:** In this app, I found that the guess hints were inverted. When a hint was too high, you would get a suggestion to go higher instead of lower. 
- **Bug 2:** I also found that if a player lost a game, they weren't able to start a new game and the game history never cleared. 
- **Fix 1:** To fix the inverted hints issue, I used Claude AI to pinpoint the root of this bug. It led me to the check_guess function which displayed the wrong hint for any guess. By switching "Go lower" to when the guess was too high, and "Go higher" for when the guess was too low, the issue was resolved. 
- **Fix 2:** To fix the new game issue, I again asked Claude AI to pinpoint the root of the problem. The issue originated from the game handler. Whenever a player lost, the game status changed to "lost" and stayed that way. The fix was to add 2 lines which changed the status to "playing" when a new game started, and cleared the guess history. 

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User enters a guess of 54
2. Game returns "Too high"
3. User enters a guess of 4 → "Too Low"
4. Score updates correctly after each guess
5. Game ends after the correct guess
6. User clicks new game 
7. Game clears out guess history and restarts game

## 🧪 Test Results

```
# pytest tests/test_game_logic.py
# tests/test_game_logic.py::test_new_game_after_loss_unblocks_play PASSED  [ 11%] 
# tests/test_game_logic.py::test_new_game_after_win_unblocks_play PASSED   [ 22%]
# tests/test_game_logic.py::test_new_game_clears_history PASSED            [ 33%]
# tests/test_game_logic.py::test_new_game_resets_attempts PASSED           [ 44%]
# tests/test_game_logic.py::test_winning_guess PASSED                      [ 55%]
# tests/test_game_logic.py::test_guess_too_high PASSED                     [ 66%]
# tests/test_game_logic.py::test_guess_too_low PASSED                      [ 77%]
# tests/test_game_logic.py::test_too_high_hint_says_go_lower PASSED        [ 88%]
# tests/test_game_logic.py::test_too_low_hint_says_go_higher PASSED        [100%]

============================== 9 passed in 0.01s ===============================
```