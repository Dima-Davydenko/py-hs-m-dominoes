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
    MAX_DIGIT_NUM = 8  # max quantity of every digit in the game

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
        computer_highest_double = self.__find_highest_double(
            self.computer_pieces)
        player_highest_double = self.__find_highest_double(
            self.player_pieces)
        if computer_highest_double > player_highest_double:
            self.computer_pieces.remove(computer_highest_double)
            self.domino_snake.append(computer_highest_double)
            self.status = Status.PLAYER_MOVE
        else:
            self.player_pieces.remove(player_highest_double)
            self.domino_snake.append(player_highest_double)
            self.status = Status.COMP_MOVE

    def __count_dots_appearance(self, dots_quantity, dominoes):
        for d in dominoes:
            for n in d:
                dots_quantity[n] += 1
        return dots_quantity

    def __take_from_stock(self, dominoes):
        if len(self.stock_pieces) > 0:
            domino_piece = self.stock_pieces.pop(
                random.randint(0, len(self.stock_pieces) - 1)
            )
            dominoes.append(domino_piece)
        else:
            print("No dominoes left in stock.")

    def __comp_move(self):
        dots_quantity = {d: 0 for d in range(self.MAX_SIDE_DOTS + 1)}
        dots_quantity = self.__count_dots_appearance(
            dots_quantity, self.domino_snake)
        dots_quantity = self.__count_dots_appearance(
            dots_quantity, self.computer_pieces)
        dom_score_indexes = {d: 0 for d in range(len(self.computer_pieces))}
        for i in range(len(self.computer_pieces)):
            dom = self.computer_pieces[i]
            score = dots_quantity[dom[0]] + dots_quantity[dom[1]]
            dom_score_indexes[i] = score
        sorted_score = dict(sorted(
            dom_score_indexes.items(), key=lambda x: x[1], reverse=True
        ))
        for index in sorted_score.keys():
            domino_piece = self.computer_pieces[index]
            if (self.__update_tail(domino_piece) or
                    self.__update_head(domino_piece)):
                self.computer_pieces.remove(domino_piece)
                return
        self.__take_from_stock(self.computer_pieces)

    def __validate_input_number_player(self, dominoes):
        head_num = self.domino_snake[0][0]
        tail_num = self.domino_snake[len(self.domino_snake) - 1][1]
        while True:
            try:
                self.domino_index = int(input())
                selected_domino = dominoes[abs(self.domino_index) - 1]
                if abs(self.domino_index) > len(self.player_pieces):
                    print("Invalid input. Please try again.")
                elif self.domino_index < 0 and head_num not in selected_domino:
                    print("Invalid input. Please try again.")
                elif self.domino_index > 0 and tail_num not in selected_domino:
                    print("Invalid input. Please try again.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please try again.")

    def __update_head(self, domino_piece):
        head_num = self.domino_snake[0][0]
        if head_num == domino_piece[1]:
            self.domino_snake.insert(0, domino_piece)
            return True
        elif head_num == domino_piece[0]:
            domino_piece.reverse()
            self.domino_snake.insert(0, domino_piece)
            return True
        return False

    def __update_tail(self, domino_piece):
        tail_num = self.domino_snake[len(self.domino_snake) - 1][1]
        if tail_num == domino_piece[0]:
            self.domino_snake.append(domino_piece)
            return True
        elif tail_num == domino_piece[1]:
            domino_piece.reverse()
            self.domino_snake.append(domino_piece)
            return True
        return False

    def __update_player_pieces(self):
        domino_piece = self.player_pieces[abs(self.domino_index) - 1]
        if self.domino_index > 0 and self.__update_tail(domino_piece):
            self.player_pieces.remove(domino_piece)
        elif self.domino_index < 0 and self.__update_head(domino_piece):
            self.player_pieces.remove(domino_piece)
        elif self.domino_index == 0:
            self.__take_from_stock(self.player_pieces)

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
            self.__validate_input_number_player(self.player_pieces)
            self.__update_player_pieces()
            self.status = Status.COMP_MOVE
        elif self.status == Status.COMP_MOVE:
            self.__comp_move()
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
