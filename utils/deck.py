
def create_card(rank:str,suite:str) -> dict:
    val_high_card = {"J":11,"Q":12,"K":13,"A":14}
    if rank.isdigit():
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


def create_deck() -> list[dict]:
    deck = []
    for i in range(2,15):
        if i <= 10:
            deck.append(create_card(str(i),"S"))
        else:
            if i == 11:
                deck.append(create_card("J", "S"))
            elif i == 12:
                deck.append(create_card("Q", "S"))
            elif i == 13:
                9
                deck.append(create_card("K", "S"))
            elif i == 14:
                deck.append(create_card("A", "S"))

    for i in range(2,15):
        if i <= 10:
            deck.append(create_card(str(i),"H"))
        else:
            if i == 11:
                deck.append(create_card("J", "H"))
            elif i == 12:
                deck.append(create_card("Q", "H"))
            elif i == 13:
                deck.append(create_card("K", "H"))
            elif i == 14:
                deck.append(create_card("A", "H"))

    for i in range(2,15):
        if i <= 10:
            deck.append(create_card(str(i),"C"))
        else:
            if i == 11:
                deck.append(create_card("J", "C"))
            elif i == 12:
                deck.append(create_card("Q", "C"))
            elif i == 13:
                deck.append(create_card("K", "C"))
            elif i == 14:
                deck.append(create_card("A", "C"))
    for i in range(2,15):
        if i <= 10:
            deck.append(create_card(str(i),"D"))
        else:
            if i == 11:
                deck.append(create_card("J", "D"))
            elif i == 12:
                deck.append(create_card("Q", "D"))
            elif i == 13:
                deck.append(create_card("K", "D"))
            elif i == 14:
                deck.append(create_card("A", "D"))
    return deck

# def shuffle(deck: list[dict]) -> list[dict]:
#     return  []
print(create_deck())

