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
            val = str(input("Change an A from 11 points to 1 point? (Y or N): "))
            print val + "AAAAAAA"
            if val != "Y" and val != "N":
                print ("Please answer with Y or N")
            elif val == "Y":
                self.deck[i].change_points(1)

            print ("Your cards are " + str(self.print_cards()) + ", Total is " +  str(self.sum_cards()) + "\n")

    def done(self):
        self.not_done = False

    def get_done(self):
        return self.not_done

def blackjack(num):
    deck = Deck()
    players = []
    players_done = []
    for player in range(0, num):
        player_cards = Hand()
        player_cards.add_card(deck.draw(2))
        players.append(player_cards)

        # Here you would dm each player their cards
        print ("Player " + str(player + 1) + "'s cards are " + player_cards.print_cards())

    print ("")

    counter = 0
    while counter < len(players):
        for player in range(len(players)):
            if players[player].sum_cards() < 21 and players[player].get_done():
                print ("Player " + str(player + 1) + ", your cards are " + str(players[player].print_cards())) + ", Total is " + str(players[player].sum_cards())
                ask_for_card = True
                while ask_for_card:
                    name = str(input("Hit? (Y or N): "))
                    if name != "Y" and name != "N":
                        print ("Please answer with Y or N\n")
                    elif name == "Y":
                        ask_for_card = False
                        players[player].add_card(deck.draw(1))
                        sum = players[player].sum_cards()
                        print ("Your cards are " + str(players[player].print_cards()) + ", Total is " +  str(sum) + "\n")
                        if sum > 21:
                            players[player].ask_A()
                            sum = players[player].sum_cards()
                            if sum > 21:
                                counter += 1
                                players[player].done()
                                print ("You lose!")
                        ask_for_card = False
                    else:
                        players_done.append(players[player])
                        players[player].done()
                        counter += 1
                        ask_for_card = False
                    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    max_val = -1
    max_index = -1
    for player in range(len(players_done)):
        if int(players_done[player].sum_cards()) > max_val:
            max_val = players_done[player].sum_cards()
            max_index = player

    print ("The Winner is Player " + str(max_index + 1) + " with " + str(max_val) + " points!")

print (blackjack(5))
