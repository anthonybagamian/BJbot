import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
# from blackjack_simple.py import *
import time



client = discord.Client()


#client = commands.Bot(command_prefix='$')

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

#handles all events
#event is when something happens which triggers something else to happen
@client.event
#runs when bot has connected to the discord
async def on_ready():
    print("Bot is ready!")
    print(client.user.name)
    print(client.user.id)

@client.event
async def on_message(message):
    #.message.content is content of message
    if message.content == "!blackjack":
        #respond in channel that the message was given (command trigger)
        global deck, dealer_cards, players, player_cards
        deck = Deck()
        dealer_cards = Hand()
        dealer_cards.add_card(deck.draw(2))
        players = [dealer_cards]

        player_cards = Hand()
        player_cards.add_card(deck.draw(2))
        players.append(player_cards)
        await message.author.send("Blackjack starting, type !dealcards to see cards")
    elif message.content == ("!dealcards"):
        # DEALER CODE
        sum = -1
        while players[0].not_done:
            sum = players[0].sum_cards()
            if sum >= 17:
                players[0].done()
            else:
                players[0].add_card(deck.draw(1))
        if player_cards.sum_cards() == 21 and len(player_cards.get_cards()) == 2:
            player_sum = players[1].sum_cards()
            dealer_sum = players[0].sum_cards()
            if player_sum != dealer_sum or len(players[1].get_cards()) != len(players[1].get_cards()):
                await message.author.send("BLACKJACK! You Win! Type !Score to see your score.")
            else:
                await message.author.send("You tied! Type !Score to see your score")
        else:
            await message.author.send("Your cards are " + player_cards.print_cards() + ", Total Score: " + str(player_cards.sum_cards()) + "\nDealer has " + players[0].dealer_print() + "\nType !Yes to hit and !No to stay")
    elif message.content == ("!No"):
        player_sum = players[1].sum_cards()
        dealer_sum = players[0].sum_cards()
        print (player_sum, dealer_sum)
        if player_sum > 21:
            await message.author.send("You lose to dealer... Type !Score to see score")
        elif dealer_sum > 21 or player_sum > dealer_sum:
            await message.author.send("You beat the dealer! Type !Score to see score")
        elif player_sum == dealer_sum:
            await message.author.send("You tie with the dealer Type !Score to see score")
        elif dealer_sum > player_sum:
            await message.author.send("You lose to dealer... Type !Score to see score")
        else:
            await message.author.send("I don't know.......")
    elif message.content == ("!Yes"):
        players[1].add_card(deck.draw(1))
        sum = players[1].sum_cards()
        if sum > 21:
            players[1].ask_A()
            sum = players[1].sum_cards()
            if sum > 21:
                players[1].done()
                await message.author.send("Bust! You lose! Type !Score to see score")
        elif sum == 21 and len(players[1].get_cards()) == 2:
            await message.author.send("BLACKJACK! Type !Score to see score")
            players[1].done()
        elif sum < 21:
            await message.author.send("Your cards are " + player_cards.print_cards() + ", Total Score: " + str(player_cards.sum_cards()) + "\nDealer has " + players[1].dealer_print() + "\nType !Yes to hit and !No to stay")
    elif message.content == ("!Score"):
        player_sum = players[1].sum_cards()
        dealer_sum = players[0].sum_cards()
        await message.author.send("Scores: You: " + str(player_sum) + " vs. Dealer: " + str(dealer_sum) + "\nType !blackjack to play again")








#tells client what bot to use (login information)
client.run("NDkwMzQ1MzcwNTEwMTYzOTY5.Dn7EbQ.JkjrpApmhu6E7lcee4oNT_lP5Ho")
