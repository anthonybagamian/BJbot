import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
from Blackjack import *
import time



client = discord.Client()


#client = commands.Bot(command_prefix='$')

players = 0
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
    Blackjack = False
    #.message.content is content of message
    if message.content == "!Blackjack":
        #respond in channel that the message was given (command trigger)
        await message.channel.send("Type 1 to play, !blackjackstart to start, Type 0 to end Blackjack")
        Blackjack = True
    elif message.content == ("!blackjackstart"):
        await message.author.Blackjack.send("")
        player += 1


    #     players += 1
    # print (players)

# @client.event
# async def start_blackjack(message):
#     # on_message("!Blackjack")
#     if message.content == "!blackjackstart":
#         # players = str(players)
<<<<<<< HEAD
=======
=======
async def on_message(message, Blackjack, players):
    print('!!!')
    #.message.content is content of message
    if message.content == "!Blackjack":
        #respond in channel that the message was given (command trigger)
        await message.channel.send("Type 1 to play, Type 2 to start, Type 0 to end Blackjack")
        await Blackjack = True
    if message.content == "1" and Blackjack == True:
        await players += 1
    if message.content == "2" and Blackjack == True:
<<<<<<< HEAD
        await players = str(players)
        await message.channel.send("Blackjack is starting. Cards are in DMs. " + players + " in game.")
=======
        players = str(players)
        await message.channel.send("Blackjack is starting. Cards are in DMs. " + players + "in game.")
>>>>>>> 3a3594ef034655d683c2b389d7df536195697136
>>>>>>> 69cf4245670efc33d86f0f3f310a0cab7c5d8c88
>>>>>>> 3acc29c33b3c9bb128ac857be9e036d628c04a97







#tells client what bot to use (login information)
client.run("NDkwMzQ1MzcwNTEwMTYzOTY5.Dn7EbQ.JkjrpApmhu6E7lcee4oNT_lP5Ho")
