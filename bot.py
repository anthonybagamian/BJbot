import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
# from blackjack_simple.py import *
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

    elif message.content == ("!blackjackstart"):
        await message.author.send("hvjv")
        await message.author.send(add())










#tells client what bot to use (login information)
client.run("NDkwMzQ1MzcwNTEwMTYzOTY5.Dn7EbQ.JkjrpApmhu6E7lcee4oNT_lP5Ho")
