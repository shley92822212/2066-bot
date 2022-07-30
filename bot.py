import discord
from discord.ext import commands

from giveaway import Giveaway
from commands import Commands

token = ''

client = commands.Bot(command_prefix="2066.")
#client = discord.Client()

giveaway = Giveaway(client)
giveaway.StartUp()

commands = Commands(client)
commands.StartUp()

@client.event
async def on_ready():
    print('Logged in as user {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if isnumeric():
        #Aoe command to yell out the taunt when a number is sent
        if int(message.content) < 106 and int(message.content) > 0:
            f = open("taunts.txt", "r")
            lines = f.readlines()
            numPhrasePair = lines[int(message.content) -1].split(',', 1)
            await message.channel.send(numPhrasePair[1])


    await client.process_commands(message)


client.run(token)
