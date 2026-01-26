import random
from enum import Enum


class Status(Enum):
    COMP_MOVE = "computer move"
    COMP_WON = "computer won"
    DRAW = "draw"
    PLAYER_MOVE = "player move"
    PLAYER_WON = "player won"


class Dominoes:
    MAX_SIDE_DOTS = 6  # maximum number of dots on one side of domino piece |:::|:::|
    START_PIECES_NUM = 7  # the number of dominoes a player has at the start of the game
    MAX_DIGIT_NUM = 8

    def __init__(self):
        self.dominoes = self.__create_dominoes_pieces()
        self.computer_pieces = []
        self.player_pieces = []
        self.stock_pieces = []
        self.domino_snake = []
        self.status = None
        self.domino_index = 0

    def __create_dominoes_pieces(self):
        dominoes = []
        for side1 in range(self.MAX_SIDE_DOTS + 1):
            side2 = side1
            while side2 <= self.MAX_SIDE_DOTS:
                domino = [side1, side2]
                dominoes.append(domino)
                side2 += 1
        return dominoes

    def shuffle_pieces(self, dominoes):
        flag = True
        while flag:
            random.shuffle(dominoes)
            for i in range(self.START_PIECES_NUM * 2):
                if dominoes[i][0] == dominoes[i][1]:
                    flag = False
                    break
        return dominoes

    def __find_highest_double(self, pieces):
        highest_double = [-1, -1]
        for piece in pieces:
            if piece[0] == piece[1] and piece[0] > highest_double[0]:
                highest_double = piece
        return highest_double

    def __set_first_move(self):
        computer_highest_double = self.__find_highest_double(self.computer_pieces)
        player_highest_double = self.__find_highest_double(self.player_pieces)
        if computer_highest_double > player_highest_double:
            self.computer_pieces.remove(computer_highest_double)
            self.domino_snake.append(computer_highest_double)
            self.status = Status.PLAYER_MOVE
        else:
            self.player_pieces.remove(player_highest_double)
            self.domino_snake.append(player_highest_double)
            self.status = Status.COMP_MOVE

    def __validate_input_number(self):
        while True:
            try:
                self.domino_index = int(input())
                if abs(self.domino_index) > len(self.player_pieces):
                    raise ValueError
                else:
                    break
            except ValueError:
                print("Invalid input. Please try again.")

    def __update_pieces_num(self, dominoes):
        if self.domino_index == 0:
            domino_piece = self.stock_pieces.pop(
                random.randint(0, len(self.stock_pieces) - 1)
            )
            dominoes.append(domino_piece)
        else:
            domino_piece = dominoes.pop(abs(self.domino_index) - 1)
            if self.domino_index > 0:
                self.domino_snake.append(domino_piece)
            elif self.domino_index < 0:
                self.domino_snake.insert(0, domino_piece)

    def __is_game_end(self):
        last_index = len(self.domino_snake) - 1
        number = self.domino_snake[0][0]
        if len(self.player_pieces) == 0:
            self.status = Status.PLAYER_WON
            return True
        elif len(self.computer_pieces) == 0:
            self.status = Status.COMP_WON
            return True
        elif number == self.domino_snake[last_index][1]:
            sum = 0
            for d in self.domino_snake:
                if number in d:
                    sum += 1
                if sum == self.MAX_DIGIT_NUM:
                    self.status = Status.DRAW
                    return True
        return False

    def __make_move(self):
        if self.status == Status.PLAYER_MOVE:
            self.__validate_input_number()
            self.__update_pieces_num(self.player_pieces)
            self.status = Status.COMP_MOVE
        elif self.status == Status.COMP_MOVE:
            index = len(self.computer_pieces)
            self.domino_index = random.randint(-index, index)
            self.__update_pieces_num(self.computer_pieces)
            self.status = Status.PLAYER_MOVE

    def setup_game(self):
        self.computer_pieces = self.dominoes[: self.START_PIECES_NUM]
        self.player_pieces = self.dominoes[
            self.START_PIECES_NUM: self.START_PIECES_NUM * 2
        ]
        self.stock_pieces = self.dominoes[self.START_PIECES_NUM * 2:]
        self.__set_first_move()

    def run_game(self, display):
        while True:
            self.__make_move()
            if self.__is_game_end():
                break
            display.display_game(self)
        display.display_game(self)
