class Display:

    def __print_domino_snake(self, dominoes):
        domino = ""
        for d in dominoes.domino_snake:
            domino = domino + str(d)
        print(domino)

    def __print_player_pieces(self, dominoes):
        print("Your pieces:")
        for i in range(len(dominoes.player_pieces)):
            print(f"{i + 1}:{dominoes.player_pieces[i]}")

    def __print_game_status(self, dominoes):
        if dominoes.status == "player":
            print("Status: It's your turn to make a move. Enter your command.")
        elif dominoes.status == "computer":
            print("Status: Computer is about to make a move. Press Enter to continue...")

    def display_game(self, dominoes):
        print("=" * 70)
        print("Stock size: {0}".format(len(dominoes.stock_pieces)))
        print("Computer pieces: {0}\n".format(len(dominoes.computer_pieces)))
        self.__print_domino_snake(dominoes)
        print()
        self.__print_player_pieces(dominoes)
        print()
        self.__print_game_status(dominoes)
