# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- The game accepted numbers outside the given range (1-100) (negative or positive). Expectation is that user would be warned that an invalid number was given and give other opportunity (whilst not counting that towards allowed guesses), however, it would just accept those numbers as valid inputs. 
- The game accepted floating numbers (counted 53.5 as 53). Similar as before, expectation is that user would be warned about invalid input, or clarification about accepting float number be given, but instead the number is accepted and rounded down.
- New game button does not work. Expectation is that user should be able to start a new round after ending one, however, the button doesn't seem to work (the level doesn't matter)
- Game's counter was off. The counter for allowed attempts is not updated appropiately and can confuse the user.

---

## 2. How did you use AI as a teammate?

- Used Claude Code as well as the extenstion for VSCode.
- Example of a correct AI suggestion: For parse_guess(), it fixed bugs for input validation by suggesting to add a check for value range, as well as not allow floats (instead of just roudning down), this was checked through test cases later.
- Example of misleading AI suggestion: While refactoring get_range_for_difficulty (), the difficulty range for Hard was set 1-200, which was noted after evaluating the code. 
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  - I ran pytest after each fix and also tested manually in the browser. If the test passed and the game behaved as expected, I considered it fixed.
- Describe at least one test you ran (manual or using pytest)
  and what it showed you about your code.
  - I ran test_float_input_is_rejected which checks that `"3.7"` returns an error instead of being accepted as `3`. Before the fix the test would have failed since the old code silently rounded it down. After the fix it passed, confirming the validation was working.
- Did AI help you design or understand any tests? How?
  - Yes, it helped generate the pytest cases for each bug. It also explained why the first three check_guess tests were failing, the function returns a tuple (outcome, message) but the tests were comparing against just a string, so they needed to unpack the result first.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  - Writing pytest cases right after fixing a bug. It forces you to actually verify the fix works and gives you a safety net if something breaks later.
- What is one thing you would do differently next time you work with AI on a coding task?
  - Review AI suggestions more carefully before accepting them. The Hard difficulty range getting changed to 1-200 was a good reminder that AI doesn't always know the intent behind the code.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  - AI generated code can look clean and complete but still have subtle logic bugs that only show up when you actually play the game. You still need to read, test, and question it like you would any other code.
