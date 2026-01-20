import random

class Dominoes:
    MAX_SIDE_DOTS = 6  # maximum number of dots on one domino piece |:::|:::|
    START_PIECES_NUM = 7  # the number of dominoes a player has at the start of the game

    def __init__(self):
        self.dominoes = self.__create_dominoes_pieces()
        self.computer_pieces = []
        self.player_pieces = []
        self.stock_pieces = []
        self.domino_snake = []
        self.status = None

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

    def __get_first_move(self, computer_pieces, player_pieces):
        computer_highest_double = self.__find_highest_double(computer_pieces)
        player_highest_double = self.__find_highest_double(player_pieces)
        return computer_highest_double if computer_highest_double > player_highest_double else player_highest_double

    def update_pieces_num(self, domino_piece):
        if domino_piece in self.computer_pieces:
            self.computer_pieces.remove(domino_piece)
            self.status = "player"
        elif domino_piece in self.player_pieces:
            self.player_pieces.remove(domino_piece)
            self.status = "computer"
        else:
            print("No such domino")
            return
        self.domino_snake.append(domino_piece)

    def setup_game(self):
        self.computer_pieces = self.dominoes[:self.START_PIECES_NUM]
        self.player_pieces = self.dominoes[
            self.START_PIECES_NUM: self.START_PIECES_NUM * 2
        ]
        self.stock_pieces = self.dominoes[self.START_PIECES_NUM * 2:]
        first_domino = self.__get_first_move(self.computer_pieces, self.player_pieces)
        self.update_pieces_num(first_domino)
