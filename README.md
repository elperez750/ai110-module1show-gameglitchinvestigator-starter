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

- [ ] Describe the game's purpose.
The purpose of the game was to guess a number in a certain range depending on the difficulty.
- [ ] Detail which bugs you found.
I found countless bugs, such as the enter key not working for guessing, guesses not being accounted for if they were even, the difficulty for normal being bigger than hard.
- [ ] Explain what fixes you applied.
I first made sure that the bugs that I mentioned were fixed. I also moved all of the game logic to logic_utils.py and made sure to keep the streamlit ui aspects in the app.py. I added test cases for all of the functions to ensure that everything was running smoothly.

## 📸 Demo

- [ ] [Insert a screenshot of your fixed, winning game here]
![alt text](image.png)



## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
