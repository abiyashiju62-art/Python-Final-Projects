# Tic-Tac-Toe Game
## About the Project
tic-tac-toe is a console-based,two-player game developed using Python.Players take turns placing their symbols,"X" and "O", on a 3x3 game broad

The objective is to place three of the same symbols in a horizontal, vertical or diagonal line to win the game. If all nine positions are filled without a winning combination, the game ends in a draw.

The game also includes additional features such as players symbol selection, score and an optional to play mutliple rounds.

## Features
### Two-Players Gameplay 
  Supports two players who take turns placing their symbols on the game borad.
### Player Symbols Selection
 Players can choose who plays as "X" in each round.The player is automatically assigned "O".
### Input Validation
 Handles non-numeric inputs,numbers outside the vaild range(1-9) and already occupied postions are filled without a winning combinations.
### Automatic Winner Detection
 Checks the player's symbols against all possible winning combination and decalres the winner automatically.
### Draw Detection
 Declares a draw when all positions are filled without a winnig combination.
### Score Tracking 
 Award one point to the winning player and maintain a sparate count of draw acoross multiple rounds.
### Replay Resets
 Allow players to start another round or exit the game after each round
### Borad Reset
 Reset the game borad at the beginning of every new round while preserving the score.

## Technologies and Concepts Used
- Programming Language : Python 3
- Code Editor : Visual Studio Code
- Python Concepts:
    - Variable and data types
    -  Lists and list indexing
    -  Functions and return statements
    - Conditional statements(**if,elif,else**)
    - Loops(**while and for**)
    - Exception handling(**try and except**)
    - User input and output
    -  Logical and comparison operators

## Requirments
- Python 3.x installed on the computer.
- Visual Studio Code (optional)
- No additional Python packages are required

## How to run
1. Install python 3 on the computer.
2. Open the project folder in Visual Studio Code.
3. Open the Tic_Tac_Toe.py file
4. Click the **Run Python File** button to execute the program.
5. The game will start in the terminal
 Alternatively, you can run the program using the terminal:
 **Python Tic_Tic_Toe.py**

## How to play
1. Press Enter to start game.
2. Choose which player will play as "X":
  - Enter 1 for player 1
  - Enter 2 for player 2
3. player 1 enters a numbers 1 and 9 select a position on the borad.
4. player 2 then enters their preferred positions.
5. The game borad is displayed after each player's move.
6. If a player enters a non-numeric value, an out-range number or   an already occupied position, an error message is displayed and the player is asked to enter another position.
7. The game continues until a player wins or borad is full.
8. A player wins by placing three symbols in a horizontal, vertical or diagonal line.
9. After each round,the score and total number of draws are displayed.
10. After each round, the score and total number of draw are displayed.
11. Players can enter Yes to start another round or No to exit the game