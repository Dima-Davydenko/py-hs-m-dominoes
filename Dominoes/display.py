from dominoes import Status


class Display:
    MAX_VISIBLE_DOM = 6
    DOM_END_NUM = 3

    def __create_domino_snake(self, dominoes, start, end):
        domino = ""
        for d in dominoes.domino_snake[start:end]:
            domino = domino + str(d)
        return domino

    def __print_domino_snake(self, dominoes):
        if len(dominoes.domino_snake) > self.MAX_VISIBLE_DOM:
            head = self.__create_domino_snake(dominoes, 0, self.DOM_END_NUM)
            tail = self.__create_domino_snake(
                dominoes, -self.DOM_END_NUM, len(dominoes.domino_snake)
            )
            body = "..."
            print(head + body + tail)
        else:
            print(self.__create_domino_snake(
                dominoes, 0, len(dominoes.domino_snake)
            ))

    def __print_player_pieces(self, dominoes):
        print("Your pieces:")
        for i in range(len(dominoes.player_pieces)):
            print(f"{i + 1}:{dominoes.player_pieces[i]}")

    def __print_game_status(self, dominoes):
        if dominoes.status == Status.PLAYER_MOVE:
            print("Status: It's your turn to make a move. Enter your command.")
        elif dominoes.status == Status.COMP_MOVE:
            print(
                "Status: Computer is about to make a move. Press Enter to continue..."
            )
            while True:
                if input() == "":
                    return
                else:
                    print('Press the "Enter" button')
        elif dominoes.status == Status.PLAYER_WON:
            print("Status: The game is over. You won!")
        elif dominoes.status == Status.COMP_WON:
            print("Status: The game is over. The computer won!")
        elif dominoes.status == Status.DRAW:
            print("Status: The game is over. It's a draw!")

    def display_game(self, dominoes):
        print("=" * 70)
        print("Stock size: {0}".format(len(dominoes.stock_pieces)))
        print("Computer pieces: {0}\n".format(len(dominoes.computer_pieces)))
        self.__print_domino_snake(dominoes)
        print()
        self.__print_player_pieces(dominoes)
        print()
        self.__print_game_status(dominoes)
