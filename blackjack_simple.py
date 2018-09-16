import random

class Card:
    def __init__(self, value, points, suit):
        self.value = value
        self.points = value
        if value in ["J", "Q", "K"]:
            self.points = 10
        elif value == "A":
            self.points = 11
        self.suit = suit

    def get_value(self):
        return self.value

    def get_points(self):
        return self.points

    def change_points(self, point_val):
        self.points = point_val

    def string( self ):
        return str(self.value) + " of " + self.suit

    def print_card(self):
        return str(self.value) + " of " + self.suit + " with " + str(self.points) + " points"

class Deck:
    def __init__(self):
        self.deck = []
        suits = ["Hearts", "Spades", "Diamonds", "Clubs"]
        cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
        for suit in suits:
            for card in cards:
                if card in ["J", "Q", "K"]:
                    points = 10
                elif card == "A":
                    points = 11
                else:
                    points = int(card)
                self.deck.append(Card(card, points, suit))

    def sum_cards(self, list_cards):
        sum = 0
        for card in self.deck:
            sum += card.get_points()
        return sum

    def draw(self, num):
        cards = []
        for i in range(0,num):
            c = random.choice(self.deck)
            cards.append(c)
            self.deck.remove(c)
        return cards

class Hand:
    def __init__(self):
        self.deck = []
        self.not_done = True

    def add_card(self, cards):
        for card in cards:
            self.deck.append(card)

    def sum_cards(self):
        sum = 0
        for card in self.deck:
            sum += card.get_points()
        return sum

    def dealer_print(self):
        return self.deck[0].string()

    def print_cards(self):
        ret_str = ""
        for card in self.deck:
            ret_str += card.string() + ", "
        return ret_str[0:len(ret_str) - 2]

    def ask_A(self):
        num_A = []
        for c in range(0, len(self.deck)):
            if self.deck[c].get_value() == "A" and self.deck[c].get_points() == 11:
                num_A.append(c)
        for i in num_A:
            print ("Your cards are " + str(self.print_cards()) + ", Total is " +  str(self.sum_cards()) + "\n")
            val = str(raw_input("Change an A from 11 points to 1 point? (Y or N): "))
            if val != "Y" and val != "N":
                print ("Please answer with Y or N")
            elif val == "Y":
                self.deck[i].change_points(1)

            print ("Your cards are " + str(self.print_cards()) + ", Total is " +  str(self.sum_cards()) + "\n")

    def done(self):
        self.not_done = False

    def get_done(self):
        return self.not_done

    def get_cards(self):
        return self.deck
def add():
    return 5+6

def blackjack():
    deck = Deck()
    dealer_cards = Hand()
    dealer_cards.add_card(deck.draw(2))
    players = [dealer_cards]

    player_cards = Hand()
    player_cards.add_card(deck.draw(2))
    players.append(player_cards)

    print ("Your cards are " + player_cards.print_cards())

    print ("")

    # ADDED THIS LINE
    print ("Dealer has " + players[1].dealer_print() + "\n")

    counter = 1

    # DEALER CODE
    sum = -1
    while players[0].not_done:
        sum = players[0].sum_cards()
        print ("DEALER SUM: " + str(sum))
        if sum >= 17:
            print ("DONE")
            players[0].done()
        else:
            players[0].add_card(deck.draw(1))

    while counter < len(players):
        player = 1
        if players[player].sum_cards() < 21 and players[player].get_done():
            print ("Your cards are " + str(players[player].print_cards())) + ", Total is " + str(players[player].sum_cards())
            # GOT RID OF THE + 1 ^^^^^ (e.g. str(player + 1) --> str(player))

            ask_for_card = True
            while ask_for_card:
                name = raw_input("Hit? (Y or N): ")
                if name != "Y" and name != "N":
                    print ("Please answer with Y or N\n")
                elif name == "Y":
                    ask_for_card = False
                    players[player].add_card(deck.draw(1))
                    sum = players[player].sum_cards()
                    if sum > 21:
                        players[player].ask_A()
                        sum = players[player].sum_cards()
                        if sum > 21:
                            counter += 1
                            players[player].done()
                            print ("Bust!")
                    if sum == 21:
                        counter += 1
                        players[player].done()
                    ask_for_card = False
                else:
                    players[player].done()
                    counter += 1
                    ask_for_card = False
                print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    # THIS SHIT HAS BEEN changed down here mans

    player_sum = players[1].sum_cards()
    dealer_sum = players[0].sum_cards()
    if player_sum > 21:
        print ("You lose to dealer...")
    elif dealer_sum > 21 or player_sum > dealer_sum:
        print ("You beat the dealer!")
    elif player_sum == dealer_sum:
        print ("You tie with the dealer")

    print ("\nScores: You: " + str(player_sum) + " vs. Dealer: " + str(dealer_sum) + "\n\n")

blackjack()
