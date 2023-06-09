# Dominoes
Simple console domino game
## About
Take turns playing classic dominoes against your computer in a race to victory.
This project is all about basic concepts, to practice by making a fun little game.
## Exaples

```
======================================================================
Stock size: 14
Computer pieces: 6

[6, 6]

Your pieces:
1:[0, 6]
2:[5, 5]
3:[4, 4]
4:[4, 6]
5:[0, 1]
6:[0, 5]
7:[1, 6]

Status: It's your turn to make a move. Enter your command.
> 7
======================================================================
Stock size: 14
Computer pieces: 6

[6, 6][6, 1]

Your pieces:
1:[0, 6]
2:[5, 5]
3:[4, 4]
4:[4, 6]
5:[0, 1]
6:[0, 5]

Status: Computer is about to make a move. Press Enter to continue...
>
```
## How to play
To make a move, the player has to specify the action they want to take. In this project, the actions are represented by integer numbers in the following manner: `{side_of_the_snake (+/-), domino_number (integer)}` or `{0}`. 

For example:
```
-6  # Take the sixth domino and place it on the left side of the snake.
6  # Take the sixth domino and place it on the right side of the snake.
0  # Take an extra piece from the stock (if it's not empty) and skip a turn or simply skip a turn if the stock is already empty by this point.
```

