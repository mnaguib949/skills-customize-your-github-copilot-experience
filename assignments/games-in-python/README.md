
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a word-guessing game in Python that uses strings, loops, conditionals, user input, and random selection. The player should guess a hidden word before running out of incorrect guesses.

## 📝 Tasks

### 🛠️ Set Up the Hidden Word

#### Description

Create the game setup by storing a predefined list of words and randomly selecting one word for the player to guess.

#### Requirements

Completed program should:

- Store at least three possible words in a predefined list.
- Randomly select one word from the list at the start of each game.
- Track the letters the player has guessed and the number of incorrect guesses remaining.

### 🛠️ Build the Guessing Game

#### Description

Write the game loop that accepts letter guesses, updates the displayed progress, and ends with the appropriate result.

#### Requirements

Completed program should:

- Accept letter guesses from the player and display the current progress in a format such as `_ _ _ _`.
- Reveal correctly guessed letters in their positions and track incorrect guesses.
- End when the player guesses the complete word or has no incorrect guesses remaining.
- Display a clear win message or lose message at the end of the game.
