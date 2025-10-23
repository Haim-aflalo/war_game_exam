import utils.deck
from utils.deck import create_deck


def create_player(name:str) -> dict:
    player = {"name":None,"hand":[],"won_pile":[]}
    if not name:
        player["name"] = "AI"
    return player

# def init_game()->dict:
#     return {}
#

# def play_round(p1:dict,p2:dict):

