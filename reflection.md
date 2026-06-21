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

When resolving the issue with starting a new game upon losing, AI gave this explanation and suggestion:

Looking at the new game handler (lines 117–121) versus the status gate (lines 123–128), the root cause is clear.

What the "New Game" button resets:


st.session_state.attempts = 0
st.session_state.secret = random.randint(1, 100)
What it does NOT reset: st.session_state.status

When you lose, line 166 sets st.session_state.status = "lost". After the new game rerun, the app hits this guard at line 123:


if st.session_state.status != "playing":
    ...
    st.error("Game over. Start a new game to try again.")
    st.stop()   # <-- execution halts here
Because status is still "lost", the condition is true, the losing message re-renders, and st.stop() prevents anything below it from executing — including the guess input and submit button. The game appears stuck even though attempts and secret were correctly reset.

The fix would be to add st.session_state.status = "playing" inside the new game handler, but since you asked only for the explanation — that single missing line in the reset block is the entire bug.

I verified this result by manually testing the issue after the solution was applied, then creating a pytest to verify the results again. 

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

In my case, AI wasn't incorrect or misleading, but it did try to handle multiple things at once when being asked for a specific issue. I only applied what was relevant at the time to keep the focus on a specific bug. 
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

After the initial fix, I manually tested everything to verify that it was working smoothly. Upon creating pytests, I also ran them to ensure the solutions worked. 

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

I ran a manual test for inverted hints. I guessed one number above and one number below the secret. After running similar manual tests and getting the expected hints, I decided this particular bug was fixed.

- Did AI help you design or understand any tests? How?

AI helped me understand how simple tests could be. It designed pytests for several cases relevant to the two bugs addressed. 
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
- This could be a testing habit, a prompting strategy, or a way you used Git.

I want to resuse asking AI the underlying logic behind a possible bug. This helps me understand the issue rather than just resolving it and moving on without learning where my code went wrong. 

- What is one thing you would do differently next time you work with AI on a coding task?

I would probably save some key prompts to reuse in other cases. 

- In one or two sentences, describe how this project changed the way you think about AI generated code.

This project has helped me realize that AI generated code has to be carefully reviewed and verfied. Prior to this project I would review AI's output, but wouldn't think to create tests verifying it. This is one extra step that ensures you're not just blindly copying and pasting code.