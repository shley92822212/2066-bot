import discord
from discord.ext import commands
import os
import random
class Giveaway:
    def __init__(self, client):
        self.client = client

    def StartUp(self):
        @self.client.command(aliases=['create', 'create giveaway'])
        @commands.has_permissions(administrator=True)
        async def create_giveaway(ctx, name, prize):
            file = None
            try:
                file = open("giveaway.txt")
            except FileNotFoundError as e:
                file = open("giveaway.txt", "w+")
                temp_list = [f"{name}\n", f"{prize}\n", "entries\n", "0\n"]
                file.writelines(temp_list)
                file.close()
                await ctx.send("Giveaway successfully created :D be happy. Use '2066.enter' to enter the giveaway")
                return
            else:
                await ctx.send("Giveaway already active, please close this giveaway first and try again.")
                return
            await ctx.send("Didnt work, either be sad or try again :)")


        @self.client.command(aliases=['close', 'close giveaway'])
        @commands.has_permissions(administrator=True)
        async def close_giveaway(ctx):
            try:
                os.remove("giveaway.txt")
            except FileNotFoundError:
                await ctx.send("No giveaway found to close :( Please create a giveaway to close")
            else:
                await ctx.send("Giveaway successfully closed. Create another giveawy")


        @self.client.command(aliases=['draw', 'draw giveaway'])
        @commands.has_permissions(administrator=True)
        async def draw_giveaway(ctx):
            file = None
            try:
                file = open("giveaway.txt", "r")
            except FileNotFoundError:
                await ctx.send("No giveaway found to draw from :( Please create a giveaway")
                return
            line_in_file = file.readlines()
            if line_in_file[3] == 0:
                await ctx.send("No users have entered this giveaway, use '2066.enter' to enter")
            else:
                await ctx.send("Drawing...")
                number_of_entries = len(line_in_file) - 5
                print(number_of_entries)
                print(len)
                rand = random.randint(0, number_of_entries)
                drawn = int(line_in_file[rand+4].replace('\n', ''))
                await ctx.send(f"{self.client.get_user(drawn).mention} won the giveaway! Congrats :D")


        @self.client.command(aliases=['info', 'giveaway info'])
        async def info_giveaway(ctx):
            file = None
            try:
                file = open("giveaway.txt", "r")
            except FileNotFoundError:
                await ctx.send("No giveaway exists currently, create a giveaway to use this command")
                return
            else:
                line_in_file = file.readlines()
                await ctx.send(f"***{line_in_file[0]}***Prize: {line_in_file[1]}Entries: {line_in_file[3]}")


        @self.client.command(aliases=['enter', 'enter giveaway'])
        async def enter_giveaway(ctx):
            file = None
            try:
                file = open("giveaway.txt")
            except FileNotFoundError:
                await ctx.send("No giveaway exists currently. Be sad")
                return
            else:
                file = open("giveaway.txt", "r")
                line_in_file = file.readlines()
                for line in line_in_file:
                    if line == f"{str(ctx.message.author.id)}\n":
                        await ctx.send(f"Error: user {self.client.get_user(ctx.message.author.id).mention} already has an entry in this giveaway.")
                        file.close()
                        return
                line_in_file[3].replace('\n', '')
                line_in_file[3] = int(line_in_file[3]) + 1
                line_in_file[3] = str(line_in_file[3]) + "\n"
                line_in_file.append(f"{str(ctx.message.author.id)}\n")
                file = open("giveaway.txt", "w")
                file.writelines(line_in_file)
                file.close()
                await ctx.send(f"sucessfully added user {self.client.get_user(ctx.message.author.id).mention} to the giveaway")