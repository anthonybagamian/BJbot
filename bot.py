import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time



client = discord.Client()
Blackjack = False
players = 0

#client = commands.Bot(command_prefix='$')


#handles all events
#event is when something happens which triggers something else to happen
@client.event
#runs when bot has connected to the discord
async def on_ready():
    print("Bot is ready!")
    print(client.user.name)
    print(client.user.id)

@client.event
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
        await players = str(players)
        await message.channel.send("Blackjack is starting. Cards are in DMs. " + players + " in game.")







#tells client what bot to use (login information)
client.run("NDkwMzQ1MzcwNTEwMTYzOTY5.Dn7EbQ.JkjrpApmhu6E7lcee4oNT_lP5Ho")
