from display import Display
from dominoes import Dominoes

if __name__ == "__main__":
    dominoes = Dominoes()
    display = Display()
    dominoes.shuffle_pieces(dominoes.dominoes)

    dominoes.setup_game()
    display.display_game(dominoes)
