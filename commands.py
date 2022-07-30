import discord
from discord.ext import commands
import os
import random
class Commands:
    def __init__(self, client):
        self.client = client

    def StartUp(self):
        @self.client.command()
        async def ping(ctx):
            await ctx.send(f'Pong xD {round(client.latency * 1000)}ms')
        @self.client.command()
        async def echo(ctx, args):
            await ctx.send(args)

    #Aoe command to yell out the taunt when a number is sent
    async def aoeCommands(self, channel, num):
        f = open("taunts.txt", "r")
        lines = f.readlines()
        numPhrasePair = lines[num -1].split(',', 1)
        await channel.send(numPhrasePair[1])