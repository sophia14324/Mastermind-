# Mastermind Game
Welcome to the Mastermind Game! This is a classic code-breaking board game that requires two players, and this version is designed for single-player use.

## Rules of the Game
The rules of the game are simple. One player creates a secret code of four colored pegs, choosing from a set of six different colors. The other player must guess the code by placing their own colored pegs in a specific order. After each guess, the code creator provides feedback by indicating which pegs are the correct color and in the correct position, and which pegs are the correct color but in the wrong position. The code breaker continues to make guesses until they correctly guess the code or they run out of turns.

## Algorithm used to create the Mastermind game
* Generate a secret code consisting of four colors, chosen randomly from a set of six possible colors.
* Allow the player to make a guess at the secret code.
* Check the guess for correctness by comparing it to the secret code. If a color in the guess is also in the secret code and appears in the same position, this is considered a "correct position." If a color in the guess is in the secret code but appears in a different position, this is considered an "incorrect position."
* Inform the player of how many colors were in the correct position and how many were in an incorrect position.
* Repeat steps 2-4 until the player either correctly guesses the secret code or runs out of attempts (typically 10).
* If the player correctly guesses the secret code, inform them of their success and end the game. If the player runs out of attempts, inform them of their failure and reveal the secret code.

## How to Play
To play the game, simply download or clone the repository and run the "mastermind.py" file using Python. Follow the prompts on the screen to make your guesses and receive feedback from the game.

## Customization Options
The game's difficulty level and appearance of the game can be adjusted through the following: You can change the number of available colors, the number of turns allowed, and the colors used to display the pegs. You can also choose to display the code at the end of the game and adjust the speed of the computer's responses.

## Dependencies
The game requires Python 3.x to run, and no additional dependencies are needed.
