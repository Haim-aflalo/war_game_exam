from game_logic.game import play_round, init_game
from utils.deck import compare_cards, create_deck

if __name__ == "__main__":
    game = init_game()
    pl_1 = game["player_1"]
    pl_2 = game["player_2"]

    play_round(pl_1,pl_2)