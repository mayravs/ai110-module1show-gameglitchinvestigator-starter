# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

  1. The hints weren't accurate. They were the opposite of what was expected.
  2. The new game button doesn't work. It should start a new game on click.
  3. Some guesses were missing from the history list. It should show all guesses submitted.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| guess of 30 | "Go higher" hint shown | "Go lower" hint shown | None |
| clicked new game button | Start a new game | Kept the same game | None |
| guess of 2 | add guess to history list | guess was missing from list | None |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

I used the Claude extension on Visual Studio

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

- AI suggested changing the messages for inverted hints. After reviewing the fix and generating tests for this change, I was able to verify that AI's suggestion for the fix was accurate.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

After the initial fix, I ran the app to verify that it was working smoothly. I also ran the tests to ensure it worked. 

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

I ran a manual test. I guessed one number above and one number below the secret. After running similar manual tests, I decided this particular bug was fixed (inverted hints)

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
