# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

  1. The hints weren't accurate. They were the opposite of what was expected.
  2. Some guesses were missing from the history list. It should show all guesses submitted.
  3. When you lose the game and click on new game, it changes the secret, but it doens't let you add new guesses and the losing message still appears

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| guess of 30 | "Go higher" hint shown | "Go lower" hint shown | None |
| Lost a game and clicked new game | new game begins | Losing message was still there and wasn't able to make a new guess | None |
| guess of 2 | add guess to history list | guess was missing from list | None |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

I used the Claude extension on Visual Studio

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

AI suggested changing the messages for inverted hints. After reviewing the fix and generating tests for this change, I was able to verify that AI's suggestion for the fix was accurate.

Same with adding 2 additional lines to update the game status when a player lost. Once those two lines were added and I ran manual tests and pytests, this fix was verfied.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

N/A
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

After the initial fix, I manually tested everything to verify that it was working smoothly. Upon creating pytests, I also ran them to ensure the solutions worked. 

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

I ran a manual test for inverted hints. I guessed one number above and one number below the secret. After running similar manual tests, I decided this particular bug was fixed (inverted hints).

- Did AI help you design or understand any tests? How?

AI helped me understand how simple tests could be. 
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
