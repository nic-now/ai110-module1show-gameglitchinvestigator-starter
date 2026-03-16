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

- [] Describe the game's purpose.

  A number guessing game where the player tries to guess a secret number within a limited number of attempts. The difficulty setting adjusts the number range and attempt limit.

- [] Detail which bugs you found.

  - `parse_guess`: silently truncated floats (e.g. `"3.7"` → `3`) and didn't validate the input range
  - `check_guess`: "Go Higher" and "Go Lower" hint messages were swapped
  - `update_score`: win score formula had an off-by-one (`+1` double-penalty); "Too High" guesses incorrectly awarded +5 points on even attempts
  - `app.py`: attempt counter initialized to 1 instead of 0; invalid inputs still consumed an attempt; new game button didn't reset `status`, `score`, or `history`

- [] Explain what fixes you applied.

  - `parse_guess`: floats now rejected with an error message; added 1–100 range validation
  - `check_guess`: swapped the hint messages to the correct directions
  - `update_score`: removed the extra `+1` from the win formula; "Too High" now always deducts 5 points like "Too Low"
  - `app.py`: initialized attempts to 0; moved attempt increment after input validation; new game now fully resets all session state including `status`, `score`, and `history`

## 📸 Demo

- [ ] [Insert a screenshot of your fixed, winning game here]


