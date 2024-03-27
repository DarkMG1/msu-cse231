import cards_B as cards #import the cards_B.py module so that you can use it in your code

# Create the deck of cards
the_deck = cards.Deck()
the_deck.shuffle()

player1_list = []
player2_list = []

for i in range(5):
    player1_list.append(the_deck.deal())
    player2_list.append(the_deck.deal())

print("Starting Hands")
print("Hand1:", player1_list)
print("Hand2:", player2_list)
print()

while True:
    player1_card = player1_list.pop(0)
    player2_card = player2_list.pop(0)
    if player1_card.rank() == player2_card.rank():
        print("Battle was 1: {}, 2: {}. Battle was a draw.".format(player1_card, player2_card))
        player2_list.append(player2_card)
        player1_list.append(player1_card)
    elif player1_card.rank() > player2_card.rank() or player1_card.rank() == 1:
        print("Battle was 1: {}, 2: {}. Player 1 wins battle.".format(player1_card, player2_card))
        player1_list.append(player1_card)
        player1_list.append(player2_card)
    else:
        print("Battle was 1: {}, 2: {}. Player 2 wins battle.".format(player1_card, player2_card))
        player2_list.append(player2_card)
        player2_list.append(player1_card)
    print("hand1:", player1_list)
    print("hand2:", player2_list)
    if len(player1_list) == 0:
        print("Player 2 wins!!!")
        break
    elif len(player2_list) == 0:
        print("Player 1 wins!!!")
        break
    keep_going = input("\n:~Keep Going: (Nn) to stop ~:").lower()
    if keep_going == "n":
        if len(player1_list) > len(player2_list):
            print("Player 1 wins!!!")
        elif len(player2_list) > len(player1_list):
            print("Player 2 wins!!!")
        else :
            print("It's a draw!!!")
        break
    else:
        continue
