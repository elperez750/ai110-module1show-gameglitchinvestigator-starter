# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

Three main glitches in the game were that when you tried to guess on even guesses, the guess would not go through. When you tried to press enter to submit a guess, it would not work even though on the screen it said you could do that. For the guesses remaining, they would not update

- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

I used Claude code for the project

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

An AI suggestion that was correct was changing the asserts when testing check_guess, since check_guess returns a tuple, not a number like it was checking before 

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

Not really an instance of the AI being incorrect, but it did not point out the redundant code fix in update_score, where we had an if statement to ultimately do the same thing if the score was high or low.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

Testing the app simutaneously was crucial to make sure that the bugs were being fixed, as well as adding test cases to my test_game_logic.py

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

  One test that I ran was on parse_guess test to make sure the floats were rounded down to the nearest integer.

- Did AI help you design or understand any tests? How?

AI helped me write the tests by identifying the edge cases for each function. For instance, in parse_guess, I tested different inputs, such as integers, floats, and no inputs at all

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.

The secret number kept changing in the original app since the number was not being saved so after each guess it would create a new number
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

I would explain that reruns will override any information for the most part unless you have it in session state, which will make sure information is kept even after refreshes.

- What change did you make that finally gave the game a stable secret number?

AI did that gang I have no idea.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  
I would definetily ask AI to create a skeleton for me where I can then customize my own logic. This is a perfect balance on using AI for quickness but also doing work yourself so that you can ensure that things are accurate or to your liking.


- What is one thing you would do differently next time you work with AI on a coding task?

I will not rely too much on AI, as it does not always know what intentions you have. I will create skeletons like I mentioned above.

- In one or two sentences, describe how this project changed the way you think about AI generated code.

I learned that AI can be used as a productivity booster and not something that does all the work.
