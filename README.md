# Battling Knights

## Overview

The game consists of four knights (Red, Blue, Green, and Yellow) who fight on a 8 x 8 chessboard and four items i.e. Axe(A), Dagger(D), MagicStaff(M), and Helmet(H).

The knights are positioned as follows:

- Red (0,0)
- Blue (7,0)
- Green (7,7)
- Yellow (0,7)

The items are position as follows:

- A (2,2)
- D (2,5)
- M (5,2)
- H (5,5)

After playing the game with the provided moves in `moves.txt` file the end result should be serialized and the output is written to `final_state.json`.

## Game modelling

The game is modelled using 6 classes:

### Knight class

The Knight class has the following attributes:

- color: str
- name: str
- position: <Pos>
- status: str 
- attack_score: int
- defence_score: int
- item: <Item>

### Item class

The Item class has the following attributes:

name: str
- full_name: str 
- rank: int
- position: Pos
- attack: int 
- defence: int

### Arena class

The Arena class has the following attribute:

- board: 2D matrix (8 X 8)

Also handles arena rendering and movements of knights and knights.

### Battle class 

The Battle class has two methods one for fight which handles the the battle between knights and kill_knight methods for killing the defeated knight.

### Play class

The play class reads the movements from   `moves.txt` and sets the board.

## Usage

This application uses only bult-in and stdlib modules but requires to uses `python 3.7` and above.

To run the app run the `run.py` module as follows:
    `python run.py`


