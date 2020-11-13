import discord
from discord.ext import commands
import random

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
client.run('Nzc2Mzc5OTQyMTI0MjU3MzAw.X60CKg.Q2UI6V7oP6YuA3gNyOvQ2-qbi7s')
@client.command(pass_context = True)
async def help(ctx):
        await ctx.send('Волкодав - команды:'
                       '1 ./help - просмотр команд.'
                       '2. /gen - цитата волка.'
                       )
