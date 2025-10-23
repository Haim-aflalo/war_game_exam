def create_card(rank:str,suite:str) -> dict:
    val_high_card = {"J":11,"Q":12,"K":13,"A":14}
    if isinstance(rank,int):
        value = int(rank)
    else:
        value = val_high_card[rank]
    return {"rank":rank,"suite":suite,"value":value}

def compare_cards(p1_card:dict, p2_card:dict) -> str:
    if p1_card["value"] > p2_card["value"]:
        return "p1"
    if p1_card["value"]< p2_card["value"]:
        return  "p2"
    else:
        return "WAR"


# def create_deck() -> list[dict]:
#     return []
#
# def shuffle(deck: list[dict]) -> list[dict]:
#     return  []

