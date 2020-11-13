
import discord
from discord.ext import commands
import random
import os
file = open("quotes.txt", 'r')
a = file.readlines()
async def on_ready():
	print('Авторизован!')
async def on_message(self,message):
        print(message)
        print('Получено сообщение')

client = commands.Bot(command_prefix = '/')
@client.command(pass_context = True)
async def gen(ctx):
        await ctx.send(random.choice(a))
        print(ctx.send)
@client.command(pass_context = True)
async def code(ctx):
        await ctx.send("Не дам код")

token = os.environ.get('BOT_TOKEN')
client.run(token)
