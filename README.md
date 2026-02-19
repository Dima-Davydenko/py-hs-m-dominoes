It's a medium rate project from the Hyperskill "Python Developer" course.\
This is a small interactive Domino game that simulates gameplay between a human and AI, incorporating game loops and validation rules.

### Setup
At the beginning of the game a full domino set has 28 unique dominoes. Then each player is handed 7 random domino pieces. The rest are used as stock (the extra pieces). All these actions are generated automatically.
To start the game, players determine the starting piece. The player with the highest double ([6,6] or [5,5] for example) will donate that domino as a starting piece for the game. After doing so, their opponent will start the game by going first. If no one has a double domino, the pieces are reshuffled and redistributed automatically.

### Take a turn
In dominoes, you can make a move by taking one of the following actions:
- Select a domino and place it on the right side of the snake -> {+ domino_number (integer)}
- Select a domino and place it on the left side of the snake -> {+ domino_number (integer)}
- Take an extra piece from the stock (if it's not empty) and skip a turn -> {0}


### The end-game condition:
One of the players runs out of pieces. The first player to do so is considered a winner.
The numbers on the ends of the snake are identical and appear within the snake 8 times. For example, the snake below will satisfy this condition:\
[5,5],[5,2],[2,1],[1,5],[5,4],[4,0],[0,5],[5,3],[3,6],[6,5]\
If this condition is satisfied, it is no longer possible to go on with this snake. Even after emptying the stock, no player will have the necessary piece. Essentially, the game has come to a permanent stop, so we have a draw.


### Example 

======================================================================\
Stock size: 12\
Computer pieces: 3


[4, 4][4, 2][2, 1][1, 0][0, 0][0, 2]


Your pieces:\
1:[2, 2]\
2:[3, 3]\
3:[5, 5]\
4:[6, 6]\
5:[4, 5]\
6:[3, 6]\
7:[5, 6]


Status: Computer is about to make a move. Press Enter to continue...


======================================================================\
Stock size: 12\
Computer pieces: 2


[4, 4][4, 2][2, 1]...[0, 0][0, 2][2, 5]


Your pieces:\
1:[2, 2]\
2:[3, 3]\
3:[5, 5]\
4:[6, 6]\
5:[4, 5]\
6:[3, 6]\
7:[5, 6]


Status: It's your turn to make a move. Enter your command.\
-5


======================================================================\
Stock size: 12\
Computer pieces: 2


[5, 4][4, 4][4, 2]...[0, 0][0, 2][2, 5]


Your pieces:\
1:[2, 2]\
2:[3, 3]\
3:[5, 5]\
4:[6, 6]\
5:[3, 6]\
6:[5, 6]


Status: Computer is about to make a move. Press Enter to continue...








