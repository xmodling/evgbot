
import discord
from discord.ext import commands
import random
import os

file = open("quotes.txt", 'r')
a = file.readlines()
client = commands.Bot(command_prefix = '/')
@client.command(pass_context = True)
async def gen(ctx):
        author = ctx.message.author
        await ctx.send(f'{author.mention},' + "\n" + ":point_up:" + random.choice(a))
@client.command(pass_context = True)
async def code(ctx):
        author = ctx.message.author
        await ctx.send(f'{author.mention},' + "\n" + "Не дам код")

token = os.environ.get('BOT_TOKEN')
client.run(token)
