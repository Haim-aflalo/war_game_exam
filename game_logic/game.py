import utils.deck
from utils.deck import create_deck, compare_cards
from utils.deck import shuffle

def create_player(name:str) -> dict:
    player = {"name":None,"hand":[],"won_pile":[]}
    if not name:
        player["name"] = "AI"
    return player

def init_game()->dict:
    game_dict = {}
    p1 = create_player("hermon")
    game_dict["player_1"] = p1
    p2 = create_player('')
    game_dict["player_2"] = p2
    game_deck = create_deck()
    deck_shuffled = shuffle(game_deck)
    game_dict["deck"] = deck_shuffled
    game_dict["player_1"]["name"] = "hermon"
    game_dict["player_1"]["hand"] = deck_shuffled[26:]
    game_dict["player_2"]["hand"] = deck_shuffled[:26]

    return game_dict

def play_round(p1:dict,p2:dict):
    p1_hand = p1["hand"]
    p2_hand = p2["hand"]
    result = compare_cards(p1["hand"][-1],p2["hand"][-1])
    if result == p1:
        p1_hand.append(p2_hand)
        p2_hand.pop(-1)
        p1["hand"] = p1_hand
        p2["hand"] = p2_hand

    elif result == p2:
        p2_hand.append(p1_hand)
        p1_hand.pop(-1)
        p1["hand"] = p1_hand
        p2["hand"] = p2_hand
        print("hel")
    else:
        return
    return


